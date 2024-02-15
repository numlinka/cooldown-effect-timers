# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import ctypes
import threading


def kill_thread(thread: threading.Thread):
    ident = thread.ident
    result = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ident), ctypes.py_object(SystemExit))
    if result == 0:
        raise ValueError("invalid thread id")
    elif result != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
