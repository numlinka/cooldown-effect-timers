# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# self
from .cool_down import CoolDown
from .effect_side import EffectSide


class Display (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill=BOTH, expand=True)


        self.frame_cooldown = ttkbootstrap.Frame(self.notebook)
        self.frame_effect_side = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_cooldown, text="技能冷却")
        self.notebook.add(self.frame_effect_side, text="技能效果")

        self.cooldown = CoolDown(self.frame_cooldown)
        self.effect_side = EffectSide(self.frame_effect_side)


    def initial(self):
        self.cooldown.initial()
        self.effect_side.initial()
