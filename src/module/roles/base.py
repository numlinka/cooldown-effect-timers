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
    cd_skill = 0                    # 元素战技 CD (秒)
    cd_burst = 0                    # 元素爆发 CD (秒)

    def __init__(self, co_cooldown: CoolDown = ..., co_effectside: EffectSide = ...):
        self.co_cooldown: CoolDown = co_cooldown
        self.co_effectside: EffectSide = co_effectside

    def switch_in(self): ...        # 切换到该角色时触发
    def switch_out(self): ...       # 切换到其他角色时触发

    def press_attack(self): ...     # 按下 普通攻击 时触发
    def press_skill(self): ...      # 按下 元素战技 时触发
    def press_burst(self): ...      # 按下 元素爆发 时触发
    def press_sprint(self): ...     # 按下 冲刺 时触发
    def press_aiming(self): ...     # 按下 瞄准 时触发
    def press_jump(self): ...       # 按下 跳跃 时触发

    def release_attack(self): ...   # 抬起 普通攻击 时触发
    def release_skill(self): ...    # 抬起 元素战技 时触发
    def release_burst(self): ...    # 抬起 元素爆发 时触发
    def release_sprint(self): ...   # 抬起 冲刺 时触发
    def release_aiming(self): ...   # 抬起 瞄准 时触发
    def release_jump(self): ...     # 抬起 跳跃 时触发


__all__ = ["BaseRoleEvent"]
