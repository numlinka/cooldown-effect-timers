# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import sys
import time
import multiprocessing
import multiprocessing.connection

# site
import inputs

# local
from constants import joystick


class AsyncListenJoystick (object):
    def __init__(self, pipe_send: multiprocessing.connection.PipeConnection):
        self._triggers_threshold = 134
        self._state_cache = {}
        self.pipe_send = pipe_send
        inputs.devices._post_init()


    def run(self):
        while True:
            try:
                events = inputs.get_gamepad()
                # joystick: inputs.GamePad = inputs.devices.gamepads[0]
                # events = joystick.read()

                for event in events:
                    event: inputs.InputEvent
                    self.handle(event.code, event.device, event.ev_type, event.state, event.timestamp)

            except inputs.UnpluggedError:
                time.sleep(1)

            except Exception as _:
                time.sleep(1)

            except KeyboardInterrupt:
                sys.exit()


    def handle(self, code: str, device: inputs.GamePad, ev_type: str, state: int, timestamp: float):
        match ev_type:
            case "Sync": ...
            case "Key": self.handle_key(code, state)
            case "Relative": ...
            case "Absolute":
                match code:
                    case "ABS_X":       self.handle_joystick(code, state)
                    case "ABS_Y":       self.handle_joystick(code, state)
                    case "ABS_RX":      self.handle_joystick(code, state)
                    case "ABS_RY":      self.handle_joystick(code, state)
                    case "ABS_Z":       self.handle_triggers(code, state)
                    case "ABS_RZ":      self.handle_triggers(code, state)
                    case "ABS_HAT0X":   self.handle_directional(code, state)
                    case "ABS_HAT0Y":   self.handle_directional(code, state)
            case "Misc": ...
            case "Switch": ...
            case "LED": ...
            case "Sound": ...
            case "Repeat": ...
            case "ForceFeedback": ...
            case "Power": ...
            case "ForceFeedbackStatus": ...
            case "Max": ...
            case "Current": ...


    def handle_key(self, code: str, state: int):
        prefix = "P" if state else "R"
        self.pipe_send.send(f"{prefix} {code}")


    def handle_triggers(self, code: str, state: int):
        actioned = self._state_cache.get(code, False)
        if actioned is False and state >= self._triggers_threshold:
            self._state_cache[code] = True
            self.handle_key(code, True)

        elif actioned is True and state < self._triggers_threshold:
            self._state_cache[code] = False
            self.handle_key(code, False)


    def handle_joystick(self, code: str, state: int):
        ...


    def handle_directional(self, code: str, state: int):
        match code:
            case "ABS_HAT0X":
                key = joystick.ABS_HAT0X_KEY[state]

                last_key = self._state_cache.get("LAST_ABS_HAT0X", None)
                if last_key is not None and last_key != "ABS_HAT0X_X":
                    self.handle_key(last_key, False)

                self._state_cache["LAST_ABS_HAT0X"] = key
                if key != "ABS_HAT0X_X":
                    self.handle_key(key, True)


            case "ABS_HAT0Y":
                key = joystick.ABS_HAT0Y_KEY[state]

                last_key = self._state_cache.get("LAST_ABS_HAT0Y", None)
                if last_key is not None and last_key != "ABS_HAT0Y_Y":
                    self.handle_key(last_key, False)

                self._state_cache["LAST_ABS_HAT0Y"] = key
                if key != "ABS_HAT0Y_Y":
                    self.handle_key(key, True)



def async_listen_joystick(pipe_send: multiprocessing.connection.PipeConnection):
    listen = AsyncListenJoystick(pipe_send)
    listen.run()


__all__ = ["AsyncListenJoystick", "async_listen_joystick"]
