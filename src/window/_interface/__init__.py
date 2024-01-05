# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import module

# self
from .roles import Roles
from .cool_down import CoolDown
from .effect_side import EffectSide
from .clock import Clock
from .help import Help
from .about import About


class Interface (object):
    def __init__(self, master: ttkbootstrap.Window):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)


        self.frame_roles = ttkbootstrap.Frame(self.notebook)
        self.frame_cooldown = ttkbootstrap.Frame(self.notebook)
        self.frame_effect_side = ttkbootstrap.Frame(self.notebook)
        self.frame_clock = ttkbootstrap.Frame(self.notebook)
        self.frame_help = ttkbootstrap.Frame(self.notebook)
        self.frame_about = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_roles, text="角色")
        self.notebook.add(self.frame_cooldown, text="冷却计时器")
        self.notebook.add(self.frame_effect_side, text="效果计时器")
        self.notebook.add(self.frame_clock, text="时钟")
        self.notebook.add(self.frame_help, text="帮助")
        self.notebook.add(self.frame_about, text="关于")

        self.roles = Roles(self.frame_roles)
        self.cooldown = CoolDown(self.frame_cooldown)
        self.effect_side = EffectSide(self.frame_effect_side)
        self.clock = Clock(self.frame_clock)
        self.help = Help(self.frame_help)
        self.about = About(self.frame_about)


    def initial(self):
        self.cooldown.initial()
        self.effect_side.initial()
        module.clock.add_event(self.clock.add_clock_count)


    def final_initial(self):
        self.roles.final_initial()
