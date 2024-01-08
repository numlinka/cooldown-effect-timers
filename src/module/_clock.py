# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import time
import threading


class Clock (object):
    def __init__(self, interval: float = 0.1):
        self._lock = threading.RLock()
        self.internal_semaphore = threading.Semaphore(0)
        self.interval = 0.1
        self.event_lst: list[threading.Event] = []

        self.set_interval(interval)

        self.task_main = threading.Thread(None, self.mainloop, "Clock", (), daemon=True)
        self.task_optupt = threading.Thread(None, self.__external_loop, "Clock-optupt", (), daemon=True)

        self._last_tick_time = 0
        self._tick_count = 0
        self._tick_consume = 0
        self._tick_delay = 0


    def set_interval(self, value: float = 0.1) -> None:
        if not isinstance(value, float):
            raise TypeError("The value type is not float.")

        with self._lock:
            self.interval = value


    def add_event(self, event: threading.Event | threading.Semaphore | object):
        if not isinstance(event, (threading.Event, threading.Semaphore)) and not callable(event):
            raise TypeError("The event type is not threading.Event or threading.Semaphore or callable.")

        with self._lock:
            self.event_lst.append(event)


    def get_tick_count(self) -> int:
        with self._lock:
            return self._tick_count


    def get_tick_consume(self) -> int:
        with self._lock:
            return self._tick_consume
        

    def get_tick_delay(self) -> int:
        with self._lock:
            return self._tick_delay


    def __external_loop(self):
        while True:
            self.internal_semaphore.acquire()
            with self._lock:
                self._tick_count += 1
                start_time = int(time.monotonic() * 1000)
                self._tick_delay = start_time - self._last_tick_time
                self._last_tick_time = start_time

                for event in self.event_lst:
                    try:
                        if isinstance(event, threading.Event):
                            event.clear()

                        elif isinstance(event, threading.Semaphore):
                            event.release()

                        elif callable(event):
                            event()

                        else:
                            ...

                    except Exception:
                        ...

                end_time = int(time.monotonic() * 1000)
                self._tick_consume = end_time - start_time


    def mainloop(self):
        start_timestamp = time.monotonic()
        tick = 0
        while True:
            self.internal_semaphore.release()

            tick += 1
            now_timestamp = time.monotonic()
            end_timestamp = start_timestamp + self.interval * tick
            difference = end_timestamp - now_timestamp

            if difference <= 0.001:
                continue

            time.sleep(difference)



    def start(self):
        self.task_main.start()
        self.task_optupt.start()
