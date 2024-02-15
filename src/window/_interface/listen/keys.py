# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import tkinter

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import core
import widgets


class VariableControl (object):
    def __init__(self, key: str, variable: tkinter.Variable):
        self.key = key
        self.variable = variable

        try: self.variable.set(core.configuration._get(key))
        except Exception as _: ...

        self.variable.trace_add("write", self.write)


    def write(self, *_):
        core.configuration._set(self.key, self.variable.get())



class Keys (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.s_width = 30

        self.v_role_1 = ttkbootstrap.StringVar()
        self.v_role_2 = ttkbootstrap.StringVar()
        self.v_role_3 = ttkbootstrap.StringVar()
        self.v_role_4 = ttkbootstrap.StringVar()
        self.v_attack = ttkbootstrap.StringVar()
        self.v_skill  = ttkbootstrap.StringVar()
        self.v_burst  = ttkbootstrap.StringVar()
        self.v_sprint = ttkbootstrap.StringVar()
        self.v_aiming = ttkbootstrap.StringVar()
        self.v_jump   = ttkbootstrap.StringVar()
        self.v_reset  = ttkbootstrap.StringVar()

        self.v_role_1_sec = ttkbootstrap.StringVar()
        self.v_role_2_sec = ttkbootstrap.StringVar()
        self.v_role_3_sec = ttkbootstrap.StringVar()
        self.v_role_4_sec = ttkbootstrap.StringVar()
        self.v_attack_sec = ttkbootstrap.StringVar()
        self.v_skill_sec  = ttkbootstrap.StringVar()
        self.v_burst_sec  = ttkbootstrap.StringVar()
        self.v_sprint_sec = ttkbootstrap.StringVar()
        self.v_aiming_sec = ttkbootstrap.StringVar()
        self.v_jump_sec   = ttkbootstrap.StringVar()
        self.v_reset_sec  = ttkbootstrap.StringVar()

        self.wsf_keys = widgets.ScrollFrame(self.master)
        self.wsf_keys.pack(fill=BOTH, expand=YES)

        self.wll_role_1 = ttkbootstrap.Label(self.wsf_keys, text="角色 - 1", anchor=W)
        self.wll_role_2 = ttkbootstrap.Label(self.wsf_keys, text="角色 - 2", anchor=W)
        self.wll_role_3 = ttkbootstrap.Label(self.wsf_keys, text="角色 - 3", anchor=W)
        self.wll_role_4 = ttkbootstrap.Label(self.wsf_keys, text="角色 - 4", anchor=W)
        self.wll_attack = ttkbootstrap.Label(self.wsf_keys, text="普通攻击", anchor=W)
        self.wll_skill  = ttkbootstrap.Label(self.wsf_keys, text="元素战技", anchor=W)
        self.wll_burst  = ttkbootstrap.Label(self.wsf_keys, text="元素爆发", anchor=W)
        self.wll_sprint = ttkbootstrap.Label(self.wsf_keys, text="冲刺",     anchor=W)
        self.wll_aiming = ttkbootstrap.Label(self.wsf_keys, text="瞄准",     anchor=W)
        self.wll_jump   = ttkbootstrap.Label(self.wsf_keys, text="跳跃",     anchor=W)
        self.wll_reset  = ttkbootstrap.Label(self.wsf_keys, text="重置",     anchor=W)
        self.wll_role_1.grid(row=0,  column=0, padx=5, pady=(5, 5), sticky=W)
        self.wll_role_2.grid(row=1,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_role_3.grid(row=2,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_role_4.grid(row=3,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_attack.grid(row=4,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_skill .grid(row=5,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_burst .grid(row=6,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_sprint.grid(row=7,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_aiming.grid(row=8,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_jump  .grid(row=9,  column=0, padx=5, pady=(0, 5), sticky=W)
        self.wll_reset .grid(row=10, column=0, padx=5, pady=(0, 5), sticky=W)

        self.wet_role_1 = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_1)
        self.wet_role_2 = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_2)
        self.wet_role_3 = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_3)
        self.wet_role_4 = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_4)
        self.wet_attack = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_attack)
        self.wet_skill  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_skill)
        self.wet_burst  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_burst)
        self.wet_sprint = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_sprint)
        self.wet_aiming = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_aiming)
        self.wet_jump   = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_jump)
        self.wet_reset  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_reset)
        self.wet_role_1.grid(row=0,  column=1, padx=(0, 5), pady=(5, 5), sticky=W)
        self.wet_role_2.grid(row=1,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_role_3.grid(row=2,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_role_4.grid(row=3,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_attack.grid(row=4,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_skill .grid(row=5,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_burst .grid(row=6,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_sprint.grid(row=7,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_aiming.grid(row=8,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_jump  .grid(row=9,  column=1, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_reset .grid(row=10, column=1, padx=(0, 5), pady=(0, 5), sticky=W)

        self.wet_role_1_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_1_sec)
        self.wet_role_2_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_2_sec)
        self.wet_role_3_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_3_sec)
        self.wet_role_4_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_role_4_sec)
        self.wet_attack_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_attack_sec)
        self.wet_skill_sec  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_skill_sec)
        self.wet_burst_sec  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_burst_sec)
        self.wet_sprint_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_sprint_sec)
        self.wet_aiming_sec = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_aiming_sec)
        self.wet_jump_sec   = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_jump_sec)
        self.wet_reset_sec  = ttkbootstrap.Entry(self.wsf_keys, textvariable=self.v_reset_sec)
        self.wet_role_1_sec.grid(row=0,  column=2, padx=(0, 5), pady=(5, 5), sticky=W)
        self.wet_role_2_sec.grid(row=1,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_role_3_sec.grid(row=2,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_role_4_sec.grid(row=3,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_attack_sec.grid(row=4,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_skill_sec .grid(row=5,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_burst_sec .grid(row=6,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_sprint_sec.grid(row=7,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_aiming_sec.grid(row=8,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_jump_sec  .grid(row=9,  column=2, padx=(0, 5), pady=(0, 5), sticky=W)
        self.wet_reset_sec .grid(row=10, column=2, padx=(0, 5), pady=(0, 5), sticky=W)


    def initial(self):
        VariableControl("action_key_role_1", self.v_role_1)
        VariableControl("action_key_role_2", self.v_role_2)
        VariableControl("action_key_role_3", self.v_role_3)
        VariableControl("action_key_role_4", self.v_role_4)
        VariableControl("action_key_attack", self.v_attack)
        VariableControl("action_key_skill",  self.v_skill)
        VariableControl("action_key_burst",  self.v_burst)
        VariableControl("action_key_sprint", self.v_sprint)
        VariableControl("action_key_aiming", self.v_aiming)
        VariableControl("action_key_jump",   self.v_jump)
        VariableControl("action_key_reset",  self.v_reset)

        VariableControl("action_key_role_1_sec", self.v_role_1_sec)
        VariableControl("action_key_role_2_sec", self.v_role_2_sec)
        VariableControl("action_key_role_3_sec", self.v_role_3_sec)
        VariableControl("action_key_role_4_sec", self.v_role_4_sec)
        VariableControl("action_key_attack_sec", self.v_attack_sec)
        VariableControl("action_key_skill_sec",  self.v_skill_sec)
        VariableControl("action_key_burst_sec",  self.v_burst_sec)
        VariableControl("action_key_sprint_sec", self.v_sprint_sec)
        VariableControl("action_key_aiming_sec", self.v_aiming_sec)
        VariableControl("action_key_jump_sec",   self.v_jump_sec)
        VariableControl("action_key_reset_sec",  self.v_reset_sec)


    def final_initial(self):
        self.wsf_keys.bin_child_widgets_bind()
