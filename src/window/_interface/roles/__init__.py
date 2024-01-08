# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import webbrowser
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import env

# self
from ._roles_arms import RolesArms
from ._save import SaveFormation
from ._load import LoadFormation


class Roles (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.wra_1 = RolesArms(self.master, 1)
        self.wra_2 = RolesArms(self.master, 2)
        self.wra_3 = RolesArms(self.master, 3)
        self.wra_4 = RolesArms(self.master, 4)

        self.wra_1.pack(side=TOP, fill=X, padx=5, pady=(5, 5))
        self.wra_2.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wra_3.pack(side=TOP, fill=X, padx=5, pady=(0, 5))
        self.wra_4.pack(side=TOP, fill=X, padx=5, pady=(0, 5))

        self.wfe_help = ttkbootstrap.Frame(self.master)
        self.wfe_save = ttkbootstrap.Frame(self.master)
        self.wfe_help.pack(side=BOTTOM, fill=X, padx=5, pady=(0, 5))
        self.wfe_save.pack(side=BOTTOM, fill=X, padx=5, pady=(0, 5))

        self.wll_look_help = ttkbootstrap.Label(self.wfe_help, text="使用方法请查看 Help ( 帮助 ) 页面")
        self.wll_afdian = ttkbootstrap.Label(self.wfe_help, text="前往爱发电赞助作者", foreground="medium purple", cursor="hand2")
        self.wll_look_help.pack(side=LEFT, fill=X)
        self.wll_afdian.pack(side=RIGHT, fill=X)

        self.wbn_load = ttkbootstrap.Button(self.wfe_save, bootstyle="outline", text="加载预设配队", command=LoadFormation)
        self.wbn_save = ttkbootstrap.Button(self.wfe_save, bootstyle="outline", text="保存当前配队", command=SaveFormation)
        self.wbn_load.pack(side=RIGHT, fill=X)
        self.wbn_save.pack(side=RIGHT, fill=X, padx=(0, 5))

        self.lst_wras = [self.wra_1, self.wra_2, self.wra_3, self.wra_4]
        self.wll_afdian.bind("<Button-1>", lambda _: webbrowser.open(env.AFDIAN), True)


    def final_initial(self):
        for wra in self.lst_wras:
            wra.final_initial()
