# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import pynput

# local
import module


class ListenMouse (object):
    def __init__(self):
        self.listen = pynput.mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)
        self.listen.name = "Listen-mouse"
        self._key_cache = {}


    def on_click(self, x, y, button, pressed):
        try:
            key = self._key_cache.get(button, None)
            if key is None:
                key = str(button)
                self._key_cache[button] = key

            module.handle.key_action(key, not pressed)

        except Exception as _:
            ...


    def on_scroll(self, x, y, dx, dy):
        try:
            if dx > 0:
                module.handle.key_action("Button.scroll_left")
            elif dx < 0:
                module.handle.key_action("Button.scroll_right")

            if dy > 0:
                module.handle.key_action("Button.scroll_up")
            elif dy < 0:
                module.handle.key_action("Button.scroll_down")

        except Exception as _:
            ...


    def start(self):
        self.listen.start()



__all__ = ["ListenMouse"]
