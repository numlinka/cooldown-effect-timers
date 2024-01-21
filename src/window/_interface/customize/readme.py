# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import constants.customize


class Readme (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master
        self.wtt_readme = ttkbootstrap.Text(self.master)
        self.wtt_readme.insert(INSERT, constants.customize.README)
        self.wtt_readme.configure(state=DISABLED)
        self.wtt_readme.pack(fill=BOTH, expand=True)

        self.wsb_readme = ttkbootstrap.Scrollbar(self.wtt_readme, orient=VERTICAL, command=self.wtt_readme.yview)
        self.wtt_readme.configure(yscrollcommand=self.wsb_readme.set)

        self.wtt_readme.bind("<Enter>", lambda *_: self.wsb_readme.pack(side="right", fill="y"), "+")
        self.wtt_readme.bind("<Leave>", lambda *_: self.wsb_readme.pack_forget(), "+")
