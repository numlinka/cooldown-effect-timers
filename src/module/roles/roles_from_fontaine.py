# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 / 来自 - 枫丹

from .base import BaseRoleEvent

class Lynette (BaseRoleEvent): ...
class Lyney (BaseRoleEvent): ...
class Freminet (BaseRoleEvent): ...
class Neuvillette (BaseRoleEvent): ...
class Wriothesley (BaseRoleEvent): ...
class Charlotte (BaseRoleEvent): ...


class Furina (BaseRoleEvent):
    # 已测试
    role_name = "芙宁娜"

    cd_skills = 20
    cd_burst = 15

    ces = "孤心沙龙"
    ceb = "万众狂欢"

    def press_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.ces, 30)

    def press_burst(self):
        self.co_cooldown.burst_set()


class Navai (BaseRoleEvent): ...


__all__ = [
    "Lynette",
    "Lyney",
    "Freminet",
    "Neuvillette",
    "Wriothesley",
    "Charlotte",
    "Furina",
    "Navai"
]
