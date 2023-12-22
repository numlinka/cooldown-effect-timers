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


    def set_role(self, serial: int, role: str | roles.BaseRoleEvent, *args):
        """
        ## 设置角色

        serial: 指定角色序号 *必须
        role: 角色名称 或 角色事件类 ( 不是对象 )
        """
        if role is None:
            return

        if not isinstance(serial, int):
            raise TypeError

        if not 1 <= serial <= 4:
            raise ValueError

        if isinstance(role, str):
            if role == "":
                return

            if role not in roles.roles_table:
                raise ValueError

            class_ = roles.roles_table[role]

        else:
            class_ = role

        if not inspect.isclass(class_):
            raise TypeError

        if not issubclass(class_, roles.BaseRoleEvent):
            raise TypeError

        unit = class_(module.cooldown, module.effectside, *args)
        unit: roles.BaseRoleEvent
        self.rolesobs[serial] = unit

        save_name = role if isinstance(role, str) else ""

        match serial:
            case 1: core.configuration.role_1.set(save_name)
            case 2: core.configuration.role_2.set(save_name)
            case 3: core.configuration.role_3.set(save_name)
            case 4: core.configuration.role_4.set(save_name)

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
