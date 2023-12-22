# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# self
from .roles import Roles
from .cool_down import CoolDown
from .effect_side import EffectSide


class Interface (object):
    def __init__(self, master: ttkbootstrap.Window):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)


        self.frame_roles = ttkbootstrap.Frame(self.notebook)
        self.frame_cooldown = ttkbootstrap.Frame(self.notebook)
        self.frame_effect_side = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_roles, text="Roles")
        self.notebook.add(self.frame_cooldown, text="Cooldown")
        self.notebook.add(self.frame_effect_side, text="Effect Side")

        self.roles = Roles(self.frame_roles)
        self.cooldown = CoolDown(self.frame_cooldown)
        self.effect_side = EffectSide(self.frame_effect_side)


    def initial(self):
        self.roles.initial()
        self.cooldown.initial()
