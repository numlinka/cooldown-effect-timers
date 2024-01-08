# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import tkinter

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import core
import window


class CoolDown (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.c_interval_now = core.configuration.window_cooldown_interval
        self.c_interval_min = 20
        self.c_interval_max = 200

        self.v_moving_block = ttkbootstrap.BooleanVar()
        self.v_interval = ttkbootstrap.IntVar()
        self.v_interval_indirect = ttkbootstrap.IntVar()

        self.v_moving_block.set(False)
        self.v_interval.set(self.c_interval_now)
        self.v_interval_indirect.set(self.c_interval_now)

        self.wfe_moving_block = ttkbootstrap.Frame(self.master)
        self.wfe_interval = ttkbootstrap.Frame(self.master)
        self.wfe_moving_block.pack(side="top", fill="x", padx=5, pady=5)
        self.wfe_interval.pack(side="top", fill="x", padx=5, pady=(0, 5))

        self.wll_moving_block = ttkbootstrap.Label(self.wfe_moving_block, text="显示移动块 (按住可拖动悬浮窗)")
        self.wcb_moving_block = ttkbootstrap.Checkbutton(self.wfe_moving_block, bootstyle="success-square-toggle", variable=self.v_moving_block, command=self.bin_moving_block)
        self.wll_moving_block.pack(side="left")
        self.wcb_moving_block.pack(side="right")

        self.wll_interval = ttkbootstrap.Label(self.wfe_interval, text="角色间距")
        self.wll_interval_value = ttkbootstrap.Label(self.wfe_interval, text=f"( {self.c_interval_now} )", width=10)
        self.wse_interval = tkinter.Scale(self.wfe_interval, from_=self.c_interval_min, to=self.c_interval_max, variable=self.v_interval, orient=HORIZONTAL, resolution=1, command=self.bin_interval)
        self.wsb_interval = ttkbootstrap.Spinbox(self.wfe_interval, from_=self.c_interval_min, to=self.c_interval_max, textvariable=self.v_interval_indirect, increment=1, width=5)
        self.wll_interval.pack(side="left")
        self.wll_interval_value.pack(side="left")
        self.wse_interval.pack(side="left", fill="x", expand=True, padx=(50, 5))
        self.wsb_interval.pack(side="left")

        self.v_interval_indirect.trace_add("write", self.bin_interval_indirect)


    def bin_moving_block(self, *_):
        window.cooldown.moving_blocks(self.v_moving_block.get())


    def bin_interval(self, *_):
        value = self.v_interval.get()
        self.wll_interval_value.config(text=f"( {value} )")
        self.v_interval_indirect.set(value)
        window.cooldown.set_spacing(value)
        core.configuration.window_cooldown_interval.set(value)


    def bin_interval_indirect(self, *_):
        try:
            value = self.v_interval_indirect.get()

        except Exception as _:
            return

        if self.c_interval_min <= value <= self.c_interval_max:
            self.v_interval.set(value)
            self.bin_interval()


    def initial(self):
        value = self.v_interval.get()
        window.cooldown.set_spacing(value)

