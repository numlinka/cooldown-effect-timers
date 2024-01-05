# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import random

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

        self.v_moving_block = ttkbootstrap.BooleanVar()
        self.v_baseline = ttkbootstrap.BooleanVar()
        self.v_mode = ttkbootstrap.StringVar()

        self.v_moving_block.set(False)
        self.v_baseline.set(core.configuration.window_effectside_baseline)
        self.v_mode.set(core.configuration.window_effectside_mode)

        self.wfe_moving_block = ttkbootstrap.Frame(self.master)
        self.wfe_baseline = ttkbootstrap.Frame(self.master)
        self.wfe_mode = ttkbootstrap.Frame(self.master)
        self.wfe_test = ttkbootstrap.Frame(self.master)

        self.wfe_moving_block.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wfe_baseline.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_mode.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
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
        self.wcb_mode = ttkbootstrap.Combobox(self.wfe_mode, textvariable=self.v_mode, values=ALLMODS, width=32)
        self.wll_mode.pack(side=LEFT)
        self.wcb_mode.pack(side=RIGHT)

        self.wbn_clear_all = ttkbootstrap.Button(self.wfe_test, text="清除所有效果", command=self.bin_clear)
        self.wbn_random_add = ttkbootstrap.Button(self.wfe_test, text="随机添加测试效果", command=self.bin_random_add)
        self.wbn_clear_all.pack(side=RIGHT)
        self.wbn_random_add.pack(side=RIGHT, padx=(0, 5))

        window.method.combobox_do_not_want_selection(self.wcb_mode)

        self.v_mode.trace_add("write", self.bin_mode)


    def bin_moving_block(self, *_):
        window.effectside.moving_blocks(self.v_moving_block.get())


    def bin_baseline(self, *_):
        value = self.v_baseline.get()
        window.effectside.set_baseline(value)
        core.configuration.window_effectside_baseline.set(value)


    def bin_mode(self, *_):
        mode = self.v_mode.get()
        if mode not in ALLMODS: return
        window.effectside.set_mode(mode)
        core.configuration.window_effectside_mode.set(mode)


    def bin_random_add(self, *_):
        for serial in range(4):
            serial += 1
            module.effectside.add_effect(f"测试效果 - {serial} 号位", random.randint(10, 50), serial)

        for _ in range(12):
            serial = random.randint(1, 4)
            module.effectside.add_effect(f"测试效果 - {serial} 号位", random.randint(10, 50), serial)


    def bin_clear(self, *_):
        module.effectside.clear_all_effect()


    def initial(self, *_):
        self.bin_baseline()
