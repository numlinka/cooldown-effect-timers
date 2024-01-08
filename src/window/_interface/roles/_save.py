# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os
import json

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import window


illegalchat = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']



class SaveFormation (object):
    def __init__(self, *_):
        self.window = ttkbootstrap.Toplevel("保存当前配队")
        self.window.transient(window.mainwindow)
        self.window.resizable(False, False)
        self.window.grab_set()
        self.window.focus_set()
        window.method.center_window_for_window(self.window, window.mainwindow, 300, 100, True)

        self.wfe_name = ttkbootstrap.Frame(self.window)
        self.wfe_save = ttkbootstrap.Frame(self.window)
        self.wfe_name.pack(side=TOP, fill=X, padx=5, pady=(5, 5))
        self.wfe_save.pack(side=BOTTOM, fill=X, padx=5, pady=(0, 5))

        self.wll_name = ttkbootstrap.Label(self.wfe_name, text="配对名称")
        self.wer_name = ttkbootstrap.Entry(self.wfe_name)
        self.wll_name.pack(side=LEFT)
        self.wer_name.pack(side=LEFT, fill=X, expand=True, padx=(5, 0))

        self.wbn_save = ttkbootstrap.Button(self.wfe_save, bootstyle="outline", text="保存", width=10, command=self.save)
        self.wll_warn = ttkbootstrap.Label(self.wfe_save, foreground="red", text="", anchor=W)
        self.wbn_save.pack(side=RIGHT)
        self.wll_warn.pack(side=LEFT, fill=X, padx=(0, 5))

        self.overwrite = ""
        self.wer_name.focus_set()
        self.wer_name.bind("<Return>", self.save, True)


    def save(self, *_):
        formation_name = self.wer_name.get()

        if formation_name == "":
            self.wll_warn.config(text="名称不能为空")
            self.overwrite = formation_name
            return

        for i in illegalchat:
            if i in formation_name:
                self.wll_warn.config(text="不能包含非法字符")
                self.overwrite = formation_name
                return

        target_path = os.path.join(window.env.directory.sldata.team_formation, f"{formation_name}.team-tamplate.json")

        if os.path.isfile(target_path) and self.overwrite != formation_name:
            self.wll_warn.config(text="再次点击保存覆盖已有配置")
            self.overwrite = formation_name
            return

        result = {}

        try:
            for index in range(4):
                serial = index + 1
                result[f"rule_{serial}"] = window.interface.roles.lst_wras[index].v_role
    
            for index in range(4):
                serial = index + 1
                result[f"arms_{serial}"] = window.interface.roles.lst_wras[index].v_arms

        except Exception as _:
            self.wll_warn.config(text="读取角色数据失败")
            return

        try:
            final_result = json.dumps(result, ensure_ascii=False, sort_keys=False, indent=4)

        except Exception as _:
            self.wll_warn.config(text="转换数据失败")
            return

        try:
            fileobject = open(target_path, "w", encoding="utf-8")
            fileobject.write(final_result)

        except Exception as _:
            self.wll_warn.config(text="写入文件失败")
            return

        else:
            self.window.destroy()        

        finally:
            fileobject.close()
