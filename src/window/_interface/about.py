# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import constants


class About (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master
        self.wtt_about = ttkbootstrap.Text(self.master)
        self.wtt_about.insert(INSERT, constants.TEXT_ABOUT)
        self.wtt_about.configure(state=DISABLED)
        self.wtt_about.pack(fill=BOTH, expand=True)

        self.wsb_about = ttkbootstrap.Scrollbar(self.wtt_about, orient=VERTICAL, command=self.wtt_about.yview)
        self.wtt_about.configure(yscrollcommand=self.wsb_about.set)

        self.wtt_about.bind("<Enter>", lambda *_: self.wsb_about.pack(side="right", fill="y"), "+")
        self.wtt_about.bind("<Leave>", lambda *_: self.wsb_about.pack_forget(), "+")
