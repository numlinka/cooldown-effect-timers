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
        module.cooldown.set_skills_max_cd(unit.cd_skills, serial)
        module.cooldown.set_burst_max_cd(unit.cd_burst, serial)

        unit.serial = serial


    def action_switch_roles(self, serial: int = 1):
        module.roleserial.set(int(serial))
        new_value = module.roleserial.get()
        if self.now_role == new_value:
            return

        old_value = self.now_role
        self.now_role = new_value

        self.rolesobs[old_value].switch_out()
        self.rolesobs[new_value].switch_in()


    def action_press_skills(self):
        self.rolesobs[self.now_role].press_skills()


    def action_release_skills(self):
        self.rolesobs[self.now_role].release_skills()


    def action_press_burst(self):
        self.rolesobs[self.now_role].press_burst()


    def action_release_burst(self):
        self.rolesobs[self.now_role].release_burst()


    def action_reset(self):
        module.cooldown.reset()
        module.effectside.clear_all_effect()
