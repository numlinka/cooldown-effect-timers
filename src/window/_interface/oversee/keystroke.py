# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import datetime

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import module


class Keystroke (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.v_switch = ttkbootstrap.BooleanVar()

        self.wfe_switch = ttkbootstrap.Frame(self.master)
        self.wll_switch = ttkbootstrap.Label(self.wfe_switch, text="启用按键记录")
        self.wcb_switch = ttkbootstrap.Checkbutton(self.wfe_switch, bootstyle="success-square-toggle", variable=self.v_switch, command=self.bin_switch)

        self.wtt_logging = ttkbootstrap.Text(self.master)
        self.wsb_logging = ttkbootstrap.Scrollbar(self.wtt_logging, orient=VERTICAL, command=self.wtt_logging.yview)
        self.wtt_logging.configure(yscrollcommand=self.wsb_logging.set)

        self.wtt_logging.bind("<Enter>", lambda *_: self.wsb_logging.pack(side=RIGHT, fill=Y), "+")
        self.wtt_logging.bind("<Leave>", lambda *_: self.wsb_logging.pack_forget(), "+")

        self.wfe_switch.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wll_switch.pack(side=LEFT, fill=X, padx=0, pady=0)
        self.wcb_switch.pack(side=RIGHT, fill=X, padx=(5, 0), pady=0)
        self.wtt_logging.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=(0, 5))

        self.wtt_logging.configure(state=DISABLED)
        self.wtt_logging.tag_config("P", foreground="orange red")
        self.wtt_logging.tag_config("R", foreground="gray")


    def bin_switch(self, *_):
        if self.v_switch.get():
            module.handle.set_callback(self.bin_keystroke)
        else:
            module.handle.set_callback(lambda *_: ...)


    def async_keystroke(self, key: str, ispress: bool):
        now = datetime.datetime.now()
        microsecond =now.microsecond // 1000
        time_now = "%s.%03d"%(now.strftime("%H:%M:%S"), microsecond)
        tag = "P" if ispress else "R"
        text = f"{time_now} {tag} - {key}\n"

        self.wtt_logging.configure(state=NORMAL)
        self.wtt_logging.insert(END, text, tag)
        self.wtt_logging.configure(state=DISABLED)
        self.wtt_logging.yview_moveto(1.0)


    def bin_keystroke(self, key: str, ispress: bool):
        self.master.after(0, self.async_keystroke, key, ispress)


    def initial(self):
        ...
