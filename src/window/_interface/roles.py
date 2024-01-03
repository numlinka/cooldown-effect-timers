# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import core
import module


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
        self.wcb_role = ttkbootstrap.Combobox(self.wfe_role)
        self.wcb_arms = ttkbootstrap.Combobox(self.wfe_arms)
        self.wbn_role = ttkbootstrap.Button(self.wfe_role, text="+")
        self.wbn_arms = ttkbootstrap.Button(self.wfe_arms, text="+")

        self.wll.pack(side="left", padx=0)
        self.wfe_role.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.wfe_arms.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.wcb_role.pack(side="left", fill="x", expand=True)
        self.wcb_arms.pack(side="left", fill="x", expand=True)
        self.wbn_role.pack(side="left", padx=(5, 0))
        self.wbn_arms.pack(side="left", padx=(5, 0))
        self.pack = self.wfe.pack

        self.wcb_role.bind("<<ComboboxSelected>>", self.set_role)


    def initial(self):
        self.wcb_role.config(values=[x for x in module.roles.roles_table])
        match self.serial:
            case 1: role_name = core.configuration.role_1
            case 2: role_name = core.configuration.role_2
            case 3: role_name = core.configuration.role_3
            case 4: role_name = core.configuration.role_4

        self.wcb_role.set(role_name)
        self.set_role()


    def set_role(self, *_):
        value = self.wcb_role.get()
        module.handle.set_role(self.serial, value)


class Roles (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.wra_1 = RolesArms(self.master, 1)
        self.wra_2 = RolesArms(self.master, 2)
        self.wra_3 = RolesArms(self.master, 3)
        self.wra_4 = RolesArms(self.master, 4)

        self.wra_1.pack(side="top", fill="x", padx=5, pady=(5, 5))
        self.wra_2.pack(side="top", fill="x", padx=5, pady=(0, 5))
        self.wra_3.pack(side="top", fill="x", padx=5, pady=(0, 5))
        self.wra_4.pack(side="top", fill="x", padx=5, pady=(0, 5))

        self.wll_look_help = ttkbootstrap.Label(self.master, text="使用方法请查看 Help ( 帮助 ) 页面")
        self.wll_look_help.pack(side="bottom", fill="x", padx=5, pady=(0, 5))


    def initial(self):
        for wra in [self.wra_1, self.wra_2, self.wra_3, self.wra_4]:
            wra.initial()
