# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# self
from .base import BaseRoleEvent
from . import roles_player
from . import roles_from_liyue

roles_table: dict[str: BaseRoleEvent] = {}


def initial():
    global roles_table

    roles_table.clear()
    modlst = [roles_player, roles_from_liyue]

    for mod in modlst:
        for classname in mod.__all__:
            roleclass = getattr(mod, classname)
            roleclass: BaseRoleEvent # 声明类型是让 IDE 知道, 它不是必要的
            name = roleclass.role_name
            roles_table[name] = roleclass


__all__ = [
    "BaseRoleEvent",
    "roles_table"
    ]
