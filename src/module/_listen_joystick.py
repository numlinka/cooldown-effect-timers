# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import time
import threading
import multiprocessing

# local
import module

# self
from . import _listen_joystick_async


class ListenJoystick (object):
    def __init__(self):
        self._lock = threading.RLock()
        self._last = time.monotonic()
        self.asynchronous = threading.Thread(None, self._async_loop, "Listen-controll", (), {}, daemon=True)
        self.pipe_recv, self.pipe_send = multiprocessing.Pipe()
        self.subprocess_ = multiprocessing.Process(None, _listen_joystick_async.async_listen_joystick, "AsyncListenJoystick", (self.pipe_send, ), daemon=True)


    def _async_loop(self):
        while True:
            try:
                line = self.pipe_recv.recv().strip()
                msgs = line.split(" ")

                if len(msgs) != 2:
                    continue

                state, code = msgs
                match state:
                    case "P": module.handle.key_action_press(code)
                    case "R": module.handle.key_action_release(code)

            except Exception as _:
                ...


    def wait_before_action(self):
        with self._lock:
            wait = self._last + 1 - time.monotonic()
            if wait >= 0: time.sleep(wait)
            self._last = time.monotonic()


    def bin_start(self) -> None | str:
        with self._lock:
            self.wait_before_action()
            if self.subprocess_.is_alive(): return "子监听器已在运行"

            self.subprocess_ = multiprocessing.Process(None, _listen_joystick_async.async_listen_joystick, "AsyncListenJoystick", (self.pipe_send, ), daemon=True)
            self.subprocess_.start()


    def bin_stop(self):
        with self._lock:
            self.wait_before_action()
            if not self.subprocess_.is_alive(): return "子监听器未在运行"
            self.subprocess_.kill()


    def bin_is_running(self):
        with self._lock:
            return self.subprocess_.is_alive()


    def start(self):
        self.asynchronous.start()



__all__ = ["ListenJoystick"]
