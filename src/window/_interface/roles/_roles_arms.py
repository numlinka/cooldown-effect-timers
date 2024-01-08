# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap import dialogs
from ttkbootstrap.constants import *

# local
import core
import module
from window import method


class RolesArms (object):
    def __init__(self, master: ttkbootstrap.Frame, serial: int):
        self.master = master
        self.serial = serial

        self.v_role = ""
        self.v_arms = ""

        self.wfe = ttkbootstrap.Frame(self.master)
        self.wll = ttkbootstrap.Label(self.wfe, text=f"roles - {serial}")
        self.wfe_role = ttkbootstrap.Frame(self.wfe)
        self.wfe_arms = ttkbootstrap.Frame(self.wfe)
        self.wcb_role = ttkbootstrap.Combobox(self.wfe_role, width=1)
        self.wcb_arms = ttkbootstrap.Combobox(self.wfe_arms, width=1)
        self.wbn_role = ttkbootstrap.Button(self.wfe_role, bootstyle="outline", text="+")
        self.wbn_arms = ttkbootstrap.Button(self.wfe_arms, bootstyle="outline", text="+")

        self.wll.pack(side=LEFT, padx=0)
        self.wfe_role.pack(side=LEFT, fill=X, expand=True, padx=(5, 0))
        self.wfe_arms.pack(side=LEFT, fill=X, expand=True, padx=(5, 0))
        self.wcb_role.pack(side=LEFT, fill=X, expand=True)
        self.wcb_arms.pack(side=LEFT, fill=X, expand=True)
        self.wbn_role.pack(side=LEFT, padx=(2, 0))
        self.wbn_arms.pack(side=LEFT, padx=(2, 0))
        self.pack = self.wfe.pack

        self.wcb_role.bind("<<ComboboxSelected>>", self.set_role, True)
        self.wcb_role
        method.combobox_do_not_want_selection(self.wcb_role)
        method.combobox_do_not_want_selection(self.wcb_arms)



    def final_initial(self):
        self.wcb_role.config(values=[x for x in module.roles.roles_table])
        match self.serial:
            case 1: role_name = core.configuration.role_1
            case 2: role_name = core.configuration.role_2
            case 3: role_name = core.configuration.role_3
            case 4: role_name = core.configuration.role_4

        self.set_role(name=role_name)


    def set_role(self, *_, name: str =...):
        if isinstance(name, str):
            self.wcb_role.set(name)

        else:
            name = self.wcb_role.get()

        try:
            module.handle.set_role(self.serial, name)
            self.v_role = name

        except Exception as _:
            dialogs.Messagebox.show_error(title="角色事件错误", message=f"角色 [{self.serial}] {name}\n加载失败")
            self.wcb_role.set("")
            self.v_role = ""


    def set_arms(self, *_, name: str =...):
        ...
