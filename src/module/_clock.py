# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import time
import threading


class Clock (object):
    def __init__(self, interval: float = 0.1):
        self._lock = threading.RLock()
        self.internal_signal = threading.Event()
        self.interval = 0.1
        self.event_lst: list[threading.Event] = []

        self.set_interval(interval)

        self.task_main = threading.Thread(None, self.mainloop_new, "Clock", (), daemon=True)
        self.task_optupt = threading.Thread(None, self.__external_loop, "Clock-optupt", (), daemon=True)


    def set_interval(self, value: float = 0.1) -> None:
        if not isinstance(value, float):
            raise TypeError("The value type is not float.")

        with self._lock:
            self.interval = value


    def add_event(self, event: threading.Event):
        if not isinstance(event, threading.Event):
            raise TypeError("The event type is not threading.Event.")
        
        with self._lock:
            self.event_lst.append(event)


    def __external_loop(self):
        while True:
            self.internal_signal.wait()
            self.internal_signal.clear()
            with self._lock:
                for event in self.event_lst:
                    try:
                        event.set()

                    except Exception:
                        ...


    def mainloop(self):
        while True:
            self.internal_signal.set()
            time.sleep(self.interval)


    def mainloop_new(self):
        start_timestamp = round(time.time(), 1)
        tick = 0
        while True:
            self.internal_signal.set()

            tick += 1
            now_timestamp = time.time()
            end_timestamp = start_timestamp + self.interval * tick
            difference = end_timestamp - now_timestamp

            if difference < 0:
                continue

            time.sleep(difference)



    def start(self):
        self.task_main.start()
        self.task_optupt.start()
