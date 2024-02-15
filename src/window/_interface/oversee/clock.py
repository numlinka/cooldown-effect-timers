# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import core
import module


class Clock (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.v_oversee = ttkbootstrap.BooleanVar()
        self.v_oversee.set(core.configuration.window_clock_oversee)

        self.wfe_oversee = ttkbootstrap.Frame(self.master)
        self.wfe_count = ttkbootstrap.Frame(self.master)
        self.wfe_delay = ttkbootstrap.Frame(self.master)
        self.wfe_consume = ttkbootstrap.Frame(self.master)
        self.wfe_oversee.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wfe_count.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_delay.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wfe_consume.pack(side=TOP, fill=X, padx=5, pady=(0, 5))

        self.wll_oversee = ttkbootstrap.Label(self.wfe_oversee, text="启用时钟监视 ( 这可能会带来额外的性能消耗 )")
        self.wcb_oversee = ttkbootstrap.Checkbutton(self.wfe_oversee, bootstyle="success-square-toggle", variable=self.v_oversee, command=self.bin_clock_oversee)
        self.wll_oversee.pack(side=LEFT)
        self.wcb_oversee.pack(side=RIGHT)

        self.wll_count = ttkbootstrap.Label(self.wfe_count, text="时钟信号计数 ( 脉冲信号计数 )")
        self.wll_count_value = ttkbootstrap.Label(self.wfe_count, text=0, anchor=E)
        self.wll_count.pack(side=LEFT)
        self.wll_count_value.pack(side=RIGHT, fill=X, expand=True, padx=(10, 0))

        self.wll_delay = ttkbootstrap.Label(self.wfe_delay, text="时钟信号偏差 ( 延迟 )")
        self.wll_delay_value = ttkbootstrap.Label(self.wfe_delay, text=0, anchor=E)
        self.wll_delay.pack(side=LEFT)
        self.wll_delay_value.pack(side=RIGHT, fill=X, expand=True, padx=(10, 0))

        self.wll_consume = ttkbootstrap.Label(self.wfe_consume, text="每个刻度耗时 ( ms / tick )")
        self.wll_consume_value = ttkbootstrap.Label(self.wfe_consume, text=0, anchor=E)
        self.wll_consume.pack(side=LEFT)
        self.wll_consume_value.pack(side=RIGHT, fill=X, expand=True, padx=(10, 0))


    def add_clock_count(self):
        if not self.v_oversee.get(): return

        self.wll_count_value.configure(text=str(module.clock.get_tick_count()))

        width = 5
        delay = module.clock.get_tick_delay()
        deviation = delay - 100

        if deviation == 0:
            deviation_text = "± {:_>{width}}".format(deviation, width=width)
        elif deviation < 0:
            deviation_text = "- {:_>{width}}".format(abs(deviation), width=width)
        elif deviation > 0:
            deviation_text = "+ {:_>{width}}".format(deviation, width=width)
        else:
            deviation_text = "± {:_>{width}}".format(deviation, width=width)

        delay_text = "{:_>{width}}".format(delay, width=width)

        final_text = f"{deviation_text} ( {delay_text} ) ms"
        self.wll_delay_value.configure(text=final_text)

        consume = f"{module.clock.get_tick_consume()} ms"
        self.wll_consume_value.configure(text=consume)


    def bin_clock_oversee(self, *_):
        value = self.v_oversee.get()
        core.configuration.window_clock_oversee.set(value)


    def initial(self):
        module.clock.add_event(self.add_clock_count)
