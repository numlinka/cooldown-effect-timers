# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import threading


class RoleSerial (object):
    def __init__(self):
        self._lock = threading.RLock()
        self.serial = 0


    def set(self, value: int) -> bool | None:
        if not isinstance(value, int):
            return True
        
        if not 1 <= value <= 4:
            return True
        
        with self._lock:
            self.serial = value


    def get(self) -> int:
        with self._lock:
            result = self.serial if 1 <= self.serial <= 4 else 1
            return result


    def set_value_1(self): return self.set(1)
    def set_value_2(self): return self.set(2)
    def set_value_3(self): return self.set(3)
    def set_value_4(self): return self.set(4)
