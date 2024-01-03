# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import pynput

# local
import module


class Incident (object):
    def __init__(self):
        self.task = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.task.name = "Listen"
        self.keyboard: dict[pynput.keyboard.KeyCode: bool] = {}


    def on_press(self, key):
        # 防止键盘连按消息
        pressed = self.keyboard.get(key, False)
        if pressed: return
        self.keyboard[key] = True
        self.handle(key)


    def on_release(self, key):
        try: self.keyboard[key] = False
        except Exception as _: ...
        self.handle(key, True)


    def handle(self, key, release: bool = False):
        if isinstance(key, pynput.keyboard.KeyCode):
            key = str(key)[1:-1]


        if not release:
            if key in ["1", "2", "3", "4"]:
                # module.roleserial.set(int(key))
                module.handle.action_switch_roles(int(key))

            elif key == "e":
                module.handle.action_press_skills()

            elif key == "q":
                module.handle.action_press_burst()

            elif key == "110":
                module.handle.action_reset()

        else:
            if key == "e":
                module.handle.action_release_skills()

            elif key == "q":
                module.handle.action_release_burst()


    def start(self):
        self.task.start()
