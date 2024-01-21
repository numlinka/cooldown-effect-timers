# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import constants.customize


class LuaRule (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master
        self.wtt_luarule = ttkbootstrap.Text(self.master)
        self.wtt_luarule.insert(INSERT, constants.customize.LUAROLE)
        self.wtt_luarule.configure(state=DISABLED)
        self.wtt_luarule.pack(fill=BOTH, expand=True)

        self.wsb_luarule = ttkbootstrap.Scrollbar(self.wtt_luarule, orient=VERTICAL, command=self.wtt_luarule.yview)
        self.wtt_luarule.configure(yscrollcommand=self.wsb_luarule.set)

        self.wtt_luarule.bind("<Enter>", lambda *_: self.wsb_luarule.pack(side="right", fill="y"), "+")
        self.wtt_luarule.bind("<Leave>", lambda *_: self.wsb_luarule.pack_forget(), "+")
