# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import tkinter

# site
import ttkbootstrap
from ttkbootstrap import dialogs
from ttkbootstrap.constants import *

# local
import module
import constants.curious


class Joystick (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.s_control = True

        self.wfe_control = ttkbootstrap.Frame(self.master)
        self.wfe_control.pack(side=BOTTOM, fill=X, padx=5, pady=(5, 5))

        self.wtt_curious = ttkbootstrap.Text(self.master)
        self.wtt_curious.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=(5, 0))

        self.wbn_control = ttkbootstrap.Button(self.wfe_control, text="启动手柄监听", bootstyle=(SUCCESS, OUTLINE), command=self.bin_control)
        self.wbn_control.pack(side=RIGHT)

        self.wsb_curious = ttkbootstrap.Scrollbar(self.wtt_curious, orient=VERTICAL, command=self.wtt_curious.yview)
        self.wtt_curious.configure(yscrollcommand=self.wsb_curious.set)
        self.wtt_curious.insert(END, constants.curious.CURIOUS_JOYSTICK)
        self.wtt_curious.configure(state=DISABLED)

        self.wtt_curious.bind("<Enter>", lambda *_: self.wsb_curious.pack(side=RIGHT, fill=Y), "+")
        self.wtt_curious.bind("<Leave>", lambda *_: self.wsb_curious.pack_forget(), "+")


    def sbin_control_switch(self):
        self.s_control = not self.s_control
        if self.s_control:
            self.wbn_control.configure(bootstyle=(SUCCESS, OUTLINE))
            self.wbn_control.configure(text="启动手柄监听")
        else:
            self.wbn_control.configure(bootstyle=(DANGER, OUTLINE))
            self.wbn_control.configure(text="停止手柄监听")


    def bin_control(self, *_):
        callable_ = module.listen_joystick.bin_start if self.s_control else module.listen_joystick.bin_stop
        result = callable_()
        self.sbin_control_switch()
        if result is None: return
        dialogs.Messagebox.show_error(title="手柄监听句柄错误", message=f"{result}")
