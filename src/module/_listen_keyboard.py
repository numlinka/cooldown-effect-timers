# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import pynput

# local
import module


class ListenKeyboard (object):
    def __init__(self):
        self.listen = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listen.name = "Listen-keyboard"
        self._keyaction: dict[str: bool] = {}
        self._key_cache = {}


    def on_press(self, key):
        self.handle(key)


    def on_release(self, key):
        self.handle(key, True)


    def handle(self, orkey: pynput.keyboard.Key, release: bool = False):
        try:
            key = self._key_cache.get(orkey, None)

            if key is None:
                if isinstance(orkey, pynput.keyboard.KeyCode):
                    key = str(orkey)[1:-1]

                elif not isinstance(orkey, str):
                    key = str(orkey)

                else:
                    key = str(orkey)

                self._key_cache[orkey] = key

            if not release:
                actioned = self._keyaction.get(key, False)

                if actioned: return
                self._keyaction[key] = True
                module.handle.key_action_press(key)

            else:
                self._keyaction[key] = False
                module.handle.key_action_release(key)

        except Exception as _:
            ...


    def start(self):
        self.listen.start()



__all__ = ["ListenKeyboard"]
