# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# self
from .base import BaseRoleEvent
from . import roles_player
from . import roles_from_mondstadt
from . import roles_from_liyue
from . import roles_from_inazuma
from . import roles_from_sumeru
from . import roles_from_fontaine
from . import expand_rules_lua


roles_table: dict[str: BaseRoleEvent] = {}


def initial():
    global roles_table

    roles_table.clear()
    modlst = [
        roles_player,
        roles_from_mondstadt,
        roles_from_liyue,
        roles_from_inazuma,
        roles_from_sumeru,
        roles_from_fontaine
        ]

    for mod in modlst:
        for classname in mod.__all__:
            roleclass = getattr(mod, classname)
            roleclass: BaseRoleEvent # 声明类型是让 IDE 知道, 它不是必要的
            name = roleclass.role_name
            if name == BaseRoleEvent.role_name: continue
            roles_table[name] = roleclass

    try:
        roles_table.update(expand_rules_lua.get_rule_lst())

    except Exception:
        ...



__all__ = [
    "BaseRoleEvent",
    "roles_table"
    ]
