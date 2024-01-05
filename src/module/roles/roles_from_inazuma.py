# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 / 来自 - 稻妻

from .base import BaseRoleEvent



class RaidenShogun (BaseRoleEvent):
    # 已测试
    role_name = "雷电将军"

    cd_skills = 10
    cd_burst = 18

    ces = "雷罚恶曜之眼"
    ceb = "梦想一心"

    def press_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.ces, 25 + 1.5)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 7 + 2)



__all__ = [
    "RaidenShogun"
]
