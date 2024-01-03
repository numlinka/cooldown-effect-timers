# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *


class Clock (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.v_clock = ttkbootstrap.IntVar()
        self.v_clock.set(0)

        self.wfe_clock = ttkbootstrap.Frame(self.master)
        self.wll_clock = ttkbootstrap.Label(self.wfe_clock, text="百毫秒时钟计数 ( 脉冲信号计数 )")
        self.wll_clock_value = ttkbootstrap.Label(self.wfe_clock, textvariable=self.v_clock, anchor=E)
        self.wfe_clock.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wll_clock.pack(side=LEFT)
        self.wll_clock_value.pack(side=RIGHT, fill=X, expand=True, padx=(10, 0))


    def add_clock_count(self):
        self.v_clock.set(self.v_clock.get() + 1)
