# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import constants


class Help (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master
        self.wtt_help = ttkbootstrap.Text(self.master)
        self.wtt_help.insert(INSERT, constants.TEXT_HELP)
        self.wtt_help.configure(state=DISABLED)
        self.wtt_help.pack(fill=BOTH, expand=True)

        self.wsb_help = ttkbootstrap.Scrollbar(self.wtt_help, orient=VERTICAL, command=self.wtt_help.yview)
        self.wtt_help.configure(yscrollcommand=self.wsb_help.set)

        self.wtt_help.bind("<Enter>", lambda *_: self.wsb_help.pack(side="right", fill="y"), "+")
        self.wtt_help.bind("<Leave>", lambda *_: self.wsb_help.pack_forget(), "+")
