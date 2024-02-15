# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# self
from .clock import Clock
from .keystroke import Keystroke


class Oversee (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill=BOTH, expand=True)


        self.frame_clock = ttkbootstrap.Frame(self.notebook)
        self.frame_keystroke_logging = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_clock, text="时钟监视")
        self.notebook.add(self.frame_keystroke_logging, text="按键记录")

        self.clock = Clock(self.frame_clock)
        self.keystroke_logging = Keystroke(self.frame_keystroke_logging)


    def initial(self):
        self.clock.initial()
        self.keystroke_logging.initial()
