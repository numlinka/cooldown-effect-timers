# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# self
from .keys import Keys
from .joystick import Joystick


class Listen (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill=BOTH, expand=True)


        self.frame_keys = ttkbootstrap.Frame(self.notebook)
        self.frame_joystick = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_keys, text="按键设置")
        self.notebook.add(self.frame_joystick, text="手柄设置")

        self.keys = Keys(self.frame_keys)
        self.joystick = Joystick(self.frame_joystick)

    def initial(self):
        self.keys.initial()

    def final_initial(self):
        self.keys.final_initial()
