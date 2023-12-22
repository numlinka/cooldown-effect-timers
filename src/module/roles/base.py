# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# local
from module._cool_down import CoolDown
from module._effect_side import EffectSide

class BaseRoleEvent (object):
    # information
    role_name = "未设置"            # 角色名称
    serial = 0                      # 角色序号 (由 Handle 模块设置 在这里不用管它)
    # elemental
    cd_skills = 0                   # 元素战技 CD (秒)
    cd_burst = 0                    # 元素爆发 CD (秒)

    def __init__(self, co_cooldown: CoolDown = ..., co_effectside: EffectSide = ...):
        self.co_cooldown: CoolDown = co_cooldown
        self.co_effectside: EffectSide = co_effectside

    def switch_in(self): ...        # 切换到该角色时 触发
    def switch_out(self): ...       # 切换到其他角色时 触发
    def press_skills(self): ...     # 按下 E 时触发
    def release_skills(self): ...   # 抬起 E 时触发
    def press_burst(self): ...      # 按下 Q 时触发
    def release_burst(self): ...    # 抬起 Q 时触发


__all__ = ["BaseRoleEvent"]
