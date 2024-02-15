# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 / 来自 - 蒙德

from .base import BaseRoleEvent


class Bennett (BaseRoleEvent):
    # 已测试
    role_name = "班尼特"

    cd_skill = 10.2
    cd_burst = 15

    det = "班尼特 - 热情过载 - 判断"
    ceb = "鼓舞领域"

    def press_skill(self):
        self.co_cooldown.skill_set(0, 10.2)
        self.co_effectside.set_effect(self.det, 1.7)

    def release_skill(self):
        second = self.co_effectside.get_effect_second(self.det)

        if second > 1:
            self.co_cooldown.skill_set(0, 4.2)

        elif second > 0:
            self.co_cooldown.skill_set(0, 7.5 - second)

        self.co_effectside.del_effect(self.det)


    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 12.5)



__all__ = [
    "Bennett"
]