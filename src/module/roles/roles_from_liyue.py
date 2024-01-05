# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 / 来自 - 璃月

from .base import BaseRoleEvent


class Xiangling (BaseRoleEvent):
    # 已测试
    role_name = "香菱 [ 4 命 ]"

    cd_skills = 12
    cd_burst = 20

    ces = "锅巴"
    ceb = "旋火轮"

    def press_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.ces, 7.2)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 14.5)



class Keqing (BaseRoleEvent):
    # 已测试
    role_name = "刻晴"

    cd_skills = 7.5
    cd_burst = 12

    ces1 = "雷楔"
    ces2 = "星斗归位 - 雷附魔"

    def press_skills(self):
        if self.co_effectside.exist(self.ces1):
            self.co_effectside.del_effect(self.ces1)
            self.co_effectside.set_effect(self.ces2, 5.5)

    def release_skills(self):
        if not self.co_effectside.exist(self.ces2):
            self.co_cooldown.skills_set()
            self.co_effectside.set_effect(self.ces1, 5.5)

    def press_burst(self):
        self.co_cooldown.burst_set()



class Xingqiu (BaseRoleEvent):
    # 已测试
    role_name = "行秋"

    cd_skills = 21
    cd_burst = 20

    ces = "雨帘剑"
    ceb = "虹剑势"

    def press_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.ces, 15)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ces, 15)
        self.co_effectside.set_effect(self.ceb, 15)



class HuTao (BaseRoleEvent):
    # 已测试
    role_name = "胡桃"

    cd_skills = 16
    cd_burst = 15

    ces = "彼岸蝶舞"

    def switch_out(self):
        self.co_effectside.del_effect(self.ces)

    def release_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.ces, 9)

    def press_burst(self):
        self.co_cooldown.burst_set()



class Zhongli (BaseRoleEvent):
    # 已测试
    role_name = "钟离"

    cd_skills = 12+1
    cd_burst = 12

    ces1 = "岩脊"
    ces2 = "玉璋护盾"
    cesn = "地心"

    def press_skills(self):
        self.co_cooldown.skills_set()
        self.co_effectside.set_effect(self.cesn, 1)

        if not self.co_effectside.exist(self.ces1):
            self.co_effectside.set_effect(self.ces1, 30+1)

        self.co_effectside.set_effect(self.ces2, 20+1)

    def release_skills(self):
        if self.co_effectside.exist(self.cesn):
            self.co_cooldown.set_skills_cd(4)
            self.co_effectside.del_effect(self.ces2)

    def press_burst(self):
        self.co_cooldown.burst_set()



class Yelan (BaseRoleEvent):
    # 已测试
    role_name = "夜兰"

    cd_skills = 10 + 4
    cd_burst = 18

    det = "夜兰 - 萦络纵命索 - 判断"
    ces = "络命丝"
    ceb = "玄掷玲珑"

    def press_skills(self):
        if self.co_effectside.exist(self.ces):
            self.co_cooldown.skills_set(0, 10)
            self.co_effectside.del_effect(self.ces)

        else:
            self.co_cooldown.skills_set()
            self.co_effectside.set_effect(self.det, 0.2)
            self.co_effectside.set_effect(self.ces, 4)

    def release_skills(self):
        if self.co_effectside.exist(self.det):
            self.co_cooldown.skills_set(0, 10)
            self.co_effectside.del_effect(self.det)
            self.co_effectside.del_effect(self.ces)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 15 + 1)



__all__ = [
    "Xiangling",
    "Keqing",
    "Xingqiu",
    "HuTao",
    "Zhongli",
    "Yelan"
]