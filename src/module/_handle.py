# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import inspect

# local
import core
import module

# self
from . import roles


class Handle (object):
    def __init__(self):
        self.now_role = 1
        self.rolesobs = {index: roles.BaseRoleEvent() for index in range(1, 5)}
        self.callback = lambda *_: ...


    def set_role(self, serial: int, role: str | roles.BaseRoleEvent, *args) -> None:
        """
        ## 设置角色

        serial: 指定角色序号 *必须
        role: 角色名称 或 角色事件类 ( 不是对象 )
        """
        if not isinstance(serial, int) or not 1 <= serial <= 4:
            raise ValueError("serial 必须是1到4之间的整数")

        if role is None or (isinstance(role, str) and not role):
            return

        if isinstance(role, str):
            if role not in roles.roles_table:
                raise ValueError(f"角色 {role} 不存在")

            if role.startswith("*"):
                role_class = roles.expand_rules_lua.LuaRoleEvent
                args = (roles.roles_table[role],)

            else:
                role_class = roles.roles_table[role]

        else:
            role_class = role

        if not inspect.isclass(role_class) or not issubclass(role_class, roles.BaseRoleEvent):
            raise TypeError("如果 role 不是字符串，它必须是 BaseRoleEvent 的子类")

        unit = role_class(module.cooldown, module.effectside, *args)
        unit: roles.BaseRoleEvent
        self.rolesobs[serial] = unit

        save_name = role if isinstance(role, str) else ""
        getattr(core.configuration, f"role_{serial}").set(save_name)

        # 后处理
        module.cooldown.set_skill_max_cd(unit.cd_skill, serial)
        module.cooldown.set_burst_max_cd(unit.cd_burst, serial)

        unit.serial = serial


    def set_callback(self, callback: object):
        self.callback = callback


    def action_switch_roles(self, serial: int = 1):
        module.roleserial.set(int(serial))
        new_value = module.roleserial.get()
        if self.now_role == new_value:
            return

        old_value = self.now_role
        self.now_role = new_value

        self.rolesobs[old_value].switch_out()
        self.rolesobs[new_value].switch_in()


    def action_press_attack(self):   self.rolesobs[self.now_role].press_attack()
    def action_press_skill(self):    self.rolesobs[self.now_role].press_skill()
    def action_press_burst(self):    self.rolesobs[self.now_role].press_burst()
    def action_press_sprint(self):   self.rolesobs[self.now_role].press_sprint()
    def action_press_aiming(self):   self.rolesobs[self.now_role].press_aiming()
    def action_press_jump(self):     self.rolesobs[self.now_role].press_jump()

    def action_release_attack(self): self.rolesobs[self.now_role].release_attack()
    def action_release_skill(self):  self.rolesobs[self.now_role].release_skill()
    def action_release_burst(self):  self.rolesobs[self.now_role].release_burst()
    def action_release_sprint(self): self.rolesobs[self.now_role].release_sprint()
    def action_release_aiming(self): self.rolesobs[self.now_role].release_aiming()
    def action_release_jump(self):   self.rolesobs[self.now_role].release_jump()

    def action_reset(self):
        module.cooldown.reset()
        module.effectside.clear_all_effect()


    def key_action(self, key: str, is_release: bool = False):
        if is_release:
            self.key_action_release(key)
        else:
            self.key_action_press(key)


    def key_action_press(self, key: str):
        match key:
            case core.configuration.action_key_role_1:  self.action_switch_roles(1)
            case core.configuration.action_key_role_2:  self.action_switch_roles(2)
            case core.configuration.action_key_role_3:  self.action_switch_roles(3)
            case core.configuration.action_key_role_4:  self.action_switch_roles(4)

            case core.configuration.action_key_attack:  self.action_press_attack()
            case core.configuration.action_key_skill:   self.action_press_skill()
            case core.configuration.action_key_burst:   self.action_press_burst()
            case core.configuration.action_key_sprint:  self.action_press_sprint()
            case core.configuration.action_key_aiming:  self.action_press_aiming()
            case core.configuration.action_key_jump:    self.action_press_jump()

            case core.configuration.action_key_reset:   self.action_reset()

        self.key_sec_action_press(key)
        self.callback(key, True)


    def key_action_release(self, key: str):
        match key:
            case core.configuration.action_key_attack:  self.action_release_attack()
            case core.configuration.action_key_skill:   self.action_release_skill()
            case core.configuration.action_key_burst:   self.action_release_burst()
            case core.configuration.action_key_sprint:  self.action_release_sprint()
            case core.configuration.action_key_aiming:  self.action_release_aiming()
            case core.configuration.action_key_jump:    self.action_release_jump()

        self.key_sec_action_release(key)
        self.callback(key, False)


    def key_sec_action_press(self, key: str):
        match key:
            case core.configuration.action_key_role_1_sec:  self.action_switch_roles(1)
            case core.configuration.action_key_role_2_sec:  self.action_switch_roles(2)
            case core.configuration.action_key_role_3_sec:  self.action_switch_roles(3)
            case core.configuration.action_key_role_4_sec:  self.action_switch_roles(4)

            case core.configuration.action_key_attack_sec:  self.action_press_attack()
            case core.configuration.action_key_skill_sec:   self.action_press_skill()
            case core.configuration.action_key_burst_sec:   self.action_press_burst()
            case core.configuration.action_key_sprint_sec:  self.action_press_sprint()
            case core.configuration.action_key_aiming_sec:  self.action_press_aiming()
            case core.configuration.action_key_jump_sec:    self.action_press_jump()

            case core.configuration.action_key_reset_sec:   self.action_reset()


    def key_sec_action_release(self, key: str):
        match key:
            case core.configuration.action_key_attack_sec:  self.action_release_attack()
            case core.configuration.action_key_skill_sec:   self.action_release_skill()
            case core.configuration.action_key_burst_sec:   self.action_release_burst()
            case core.configuration.action_key_sprint_sec:  self.action_release_sprint()
            case core.configuration.action_key_aiming_sec:  self.action_release_aiming()
            case core.configuration.action_key_jump_sec:    self.action_release_jump()



__all__ = ["Handle"]
