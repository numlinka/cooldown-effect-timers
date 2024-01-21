# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os
import json

# site
import ttkbootstrap
from ttkbootstrap import dialogs
from ttkbootstrap.constants import *

# local
import env
import window


illegalchat = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']



class LoadFormation (object):
    def __init__(self, *_):
        self.window = ttkbootstrap.Toplevel("加载预设配队")
        self.window.transient(window.mainwindow)
        self.window.resizable(False, False)
        self.window.grab_set()
        self.window.focus_set()
        window.method.center_window_for_window(self.window, window.mainwindow, 400, 250, True)

        self.suffix = ".team-tamplate.json"
        self.default_text = "左键单击查看\n左键双击加载\n\n右键双击删除"

        self.wfe_lst = ttkbootstrap.Frame(self.window)
        self.wfe_con = ttkbootstrap.Frame(self.window)
        self.wfe_inf = ttkbootstrap.Frame(self.window)
        self.wfe_lst.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
        self.wfe_con.pack(side=BOTTOM, fill=X, padx=(0, 5), pady=5)
        self.wfe_inf.pack(side=TOP, fill=BOTH, expand=True, padx=(0, 5), pady=(5, 0))

        self.wtv_lst = ttkbootstrap.Treeview(self.wfe_lst, show=TREE, selectmode=BROWSE)
        self.wtv_lst.pack(side=LEFT, fill=BOTH)

        self.wbn_load = ttkbootstrap.Button(self.wfe_con, bootstyle="outline", text="加载", command=self.load)
        self.wbn_del_ = ttkbootstrap.Button(self.wfe_con, bootstyle="outline", text="删除", command=self.del_)
        self.wbn_load.pack(side=RIGHT, fill=X, expand=True)
        self.wbn_del_.pack(side=RIGHT, fill=X, expand=True, padx=(0, 5))

        self.wll_info = ttkbootstrap.Label(self.wfe_inf, text=self.default_text, anchor=NW)
        self.wll_info.pack(side=TOP, fill=BOTH, expand=True)


        self.wtv_lst.column("#0", width=190)
        self.wtv_lst.bind("<<TreeviewSelect>>", self.load_lnfo)
        self.wtv_lst.bind("<Double-1>", self.load)
        self.wtv_lst.bind("<Double-3>", self.del_)
        self.load_list()



    def load_list(self, *_):
        for name in os.listdir(env.cwd.sldata.formation):
            path = os.path.join(env.cwd.sldata.formation, name)
            if not os.path.isfile(path) or not name.endswith(self.suffix):
               continue

            alias = name[:-len(self.suffix)]
            self.wtv_lst.insert("", END, alias, text=alias)


    def load_lnfo(self, *_):
        self.load(load_lnfo_only=True)


    def load(self, *_, load_lnfo_only: bool = False):
        alias = self.wtv_lst.focus()
        if alias == "": return

        path = os.path.join(env.cwd.sldata.formation, alias + self.suffix)
        if not os.path.isfile(path): return

        try:
            with open(path, "r", encoding="utf-8") as fobj: data = json.load(fobj)

        except Exception as _:
            self.wll_info.configure(text="文件格式错误\n无法解码文件内容")
            # dialogs.Messagebox.show_error(title="加载失败", message="文件格式错误\n无法解码文件内容", parent=self.window)
            return

        text = ""

        for key_prefix in ["rule", "arms"]:
            if key_prefix != "rule":
                text += "\n"

            for index in range(4):
                serial = index + 1
                key = f"{key_prefix}_{serial}"

                if key not in data:
                    text += f"- \n"
                    continue

                name = data[key]
                text += f"- {name}\n"

                if load_lnfo_only: continue
                match key_prefix:
                    case "rule": window.interface.roles.lst_wras[index].set_role(name=name)
                    case "arms": window.interface.roles.lst_wras[index].set_arms(name=name)

        text = text.strip()
        self.wll_info.configure(text=text)

        if load_lnfo_only: return
        self.window.destroy()


    def del_(self, *_):
        alias = self.wtv_lst.focus()
        if alias == "": return

        path = os.path.join(env.cwd.sldata.formation, alias + self.suffix)
        if not os.path.isfile(path): return

        self.wtv_lst.delete(alias)
        self.wll_info.configure(text=self.default_text)
        os.remove(path)
