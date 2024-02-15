# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 / 来自 - 须弥

from .base import BaseRoleEvent


class Nahida (BaseRoleEvent):
    # 已测试
    role_name = "纳西妲"

    cd_skill = 5
    cd_burst = 13.5

    det = "纳西妲 - 所闻遍计 - 判断"
    ces = "所闻遍计"
    ced = "摩耶之殿"

    def press_skill(self):
        self.co_cooldown.skill_set(..., 11.6)
        self.co_effectside.set_effect(self.ces, 5.4)
        self.co_effectside.set_effect(self.det, 0.2)

    def release_skill(self):
        if self.co_effectside.exist(self.det):
            self.co_effectside.del_effect(self.det)
            self.co_effectside.del_effect(self.ces)
            second = self.co_effectside.get_effect_second(self.det)
            self.co_cooldown.skill_set(0, 5.2 - second)


        elif self.co_effectside.exist(self.ces):
            self.co_effectside.del_effect(self.ces)
            self.co_cooldown.skill_set(0, 6.2)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ced, 15+1)


__all__ = [
    "Nahida",
]
