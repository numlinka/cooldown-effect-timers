# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import random
import tkinter

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import core
import module
import window
from constants.effect_site_mode import *


class EffectSide (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.c_amount_now = core.configuration.window_effectside_amount
        self.c_amount_min = 1
        self.c_amount_max = 20

        self.v_moving_block = ttkbootstrap.BooleanVar()
        self.v_baseline = ttkbootstrap.BooleanVar()
        self.v_mode = ttkbootstrap.StringVar()
        self.v_amount = ttkbootstrap.IntVar()
        self.v_amount_indirect = ttkbootstrap.IntVar()

        self.v_moving_block.set(False)
        self.v_baseline.set(core.configuration.window_effectside_baseline)
        self.v_mode.set(core.configuration.window_effectside_mode)
        self.v_amount.set(self.c_amount_now)
        self.v_amount_indirect.set(self.c_amount_now)

        self.wfe_moving_block = ttkbootstrap.Frame(self.master)
        self.wfe_baseline = ttkbootstrap.Frame(self.master)
        self.wfe_mode = ttkbootstrap.Frame(self.master)
        self.wfe_amount = ttkbootstrap.Frame(self.master)
        self.wfe_test = ttkbootstrap.Frame(self.master)

        self.wfe_moving_block.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wfe_baseline.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_mode.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_amount.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_test.pack(side=BOTTOM, fill=X, padx=5, pady=(0, 5))

        self.wll_moving_block = ttkbootstrap.Label(self.wfe_moving_block, text="显示移动块 (按住可拖动悬浮窗)")
        self.wcb_moving_block = ttkbootstrap.Checkbutton(self.wfe_moving_block, bootstyle="success-square-toggle", variable=self.v_moving_block, command=self.bin_moving_block)
        self.wll_moving_block.pack(side=LEFT)
        self.wcb_moving_block.pack(side=RIGHT)

        self.wll_baseline = ttkbootstrap.Label(self.wfe_baseline, text="显示基准线")
        self.wcb_baseline = ttkbootstrap.Checkbutton(self.wfe_baseline, bootstyle="success-square-toggle", variable=self.v_baseline, command=self.bin_baseline)
        self.wll_baseline.pack(side=LEFT)
        self.wcb_baseline.pack(side=RIGHT)

        self.wll_mode = ttkbootstrap.Label(self.wfe_mode, text="显示模式")
        self.wcb_mode = ttkbootstrap.Combobox(self.wfe_mode, textvariable=self.v_mode, values=ALLMODES, width=32)
        self.wll_mode.pack(side=LEFT)
        self.wcb_mode.pack(side=RIGHT)

        self.wll_amount = ttkbootstrap.Label(self.wfe_amount, text="显示数量")
        self.wll_amount_value = ttkbootstrap.Label(self.wfe_amount, text=f"( {self.c_amount_now} )", width=10)
        self.wse_interval = tkinter.Scale(self.wfe_amount, from_=self.c_amount_min, to=self.c_amount_max, variable=self.v_amount, orient=HORIZONTAL, resolution=1, command=self.bin_amount)
        self.wsb_amount = ttkbootstrap.Spinbox(self.wfe_amount, from_=self.c_amount_min, to=self.c_amount_max, textvariable=self.v_amount_indirect, increment=1, width=5)
        self.wll_amount.pack(side=LEFT)
        self.wll_amount_value.pack(side=LEFT, padx=(0, 5))
        self.wse_interval.pack(side=LEFT, fill=X, expand=True, padx=(50, 5))
        self.wsb_amount.pack(side=LEFT)

        self.wbn_clear_all = ttkbootstrap.Button(self.wfe_test, bootstyle="outline", text="清除所有效果", command=self.bin_clear)
        self.wbn_random_add = ttkbootstrap.Button(self.wfe_test, bootstyle="outline", text="随机添加测试效果", command=self.bin_random_add)
        self.wbn_clear_all.pack(side=RIGHT)
        self.wbn_random_add.pack(side=RIGHT, padx=(0, 5))

        window.method.combobox_do_not_want_selection(self.wcb_mode)
        window.method.combobox_do_not_want_selection(self.wsb_amount)

        self.v_mode.trace_add("write", self.bin_mode)
        self.v_amount_indirect.trace_add("write", self.bin_amount_indirect)


    def bin_moving_block(self, *_):
        window.effectside.moving_blocks(self.v_moving_block.get())


    def bin_baseline(self, *_):
        value = self.v_baseline.get()
        core.configuration.window_effectside_baseline.set(value)
        window.effectside.set_baseline(value)


    def bin_mode(self, *_):
        mode = self.v_mode.get()
        if mode not in ALLMODES: return
        core.configuration.window_effectside_mode.set(mode)
        window.effectside.set_mode(mode)


    def bin_amount(self, *_):
        amount = self.v_amount.get()
        self.wll_amount_value.config(text=f"( {amount} )")
        self.v_amount_indirect.set(amount)
        window.effectside.set_amount(amount)
        core.configuration.window_effectside_amount.set(amount)


    def bin_amount_indirect(self, *_):
        try:
            value = self.v_amount_indirect.get()

        except Exception as _:
            return

        if self.c_amount_min <= value <= self.c_amount_max:
            self.v_amount.set(value)
            self.bin_amount()


    def bin_random_add(self, *_):
        for serial in range(4):
            serial += 1
            second = random.randint(10, 50)
            module.effectside.add_effect(f"测试效果 - {serial} 号位", second, serial)

        for _ in range(12):
            serial = random.randint(1, 4)
            second = random.randint(10, 50)
            module.effectside.add_effect(f"测试效果 - {serial} 号位", second, serial)


    def bin_clear(self, *_):
        module.effectside.clear_all_effect()


    def initial(self, *_):
        ...
