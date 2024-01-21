# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# self
from .readme import Readme
from .luarole import LuaRule


class Customize (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill=BOTH, expand=True)


        self.frame_readme = ttkbootstrap.Frame(self.notebook)
        self.frame_luarole = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_readme, text="readme")
        self.notebook.add(self.frame_luarole, text="lua")

        self.readme = Readme(self.frame_readme)
        self.luarole = LuaRule(self.frame_luarole)
