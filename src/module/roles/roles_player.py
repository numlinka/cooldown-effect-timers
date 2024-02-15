# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# 角色 - 玩家

from .base import BaseRoleEvent


class PlayerPyro (BaseRoleEvent):
    role_name = "旅行者 - 火"


class PlayerHydro (BaseRoleEvent):
    #todo 未测试
    role_name = "旅行者 - 水"

    cd_skill = 10 + 6
    cd_burst = 20

    ces = "水纹露滴"
    ceb = "扬水制流"

    def press_skill(self):
        self.co_cooldown.skill_set()
        self.co_effectside.set_effect(self.ces, 6)

    def release_skill(self):
        if self.co_effectside.exist(self.ces):
            self.co_cooldown.set_skill_cd(10)
            self.co_effectside.del_effect(self.ces)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 4 + 1)



class PlayerHydro_Constellation_2 (BaseRoleEvent):
    # 已测试
    role_name = "旅行者 - 水 [ 2 命 ]"

    cd_skill = 10 + 6
    cd_burst = 20

    ces = "水纹露滴"
    ceb = "扬水制流"

    def press_skill(self):
        self.co_cooldown.skill_set()
        self.co_effectside.set_effect(self.ces, 6)

    def release_skill(self):
        if self.co_effectside.exist(self.ces):
            self.co_cooldown.set_skill_cd(10)
            self.co_effectside.del_effect(self.ces)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 4 + 3 + 1)



class PlayerAnemo (BaseRoleEvent):
    # 已测试
    role_name = "旅行者 - 风"

    cd_skill = 8 + 2
    cd_burst = 15

    ces = "风刃"
    ceb = "风息激荡"

    def press_skill(self):
        self.co_cooldown.skill_set()
        self.co_effectside.set_effect(self.ces, 2)

    def release_skill(self):
        if self.co_effectside.exist(self.ces):
            self.co_cooldown.set_skill_cd(6)
            self.co_effectside.del_effect(self.ces)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 6)



class PlayerElectro (BaseRoleEvent):
    # 已测试
    role_name = "旅行者 - 雷"

    cd_skill = 13.5
    cd_burst = 20

    ces = "丰穰勾玉"
    ceb = "雷霆绕身"

    def press_skill(self):
        self.co_cooldown.skill_set()
        self.co_effectside.set_effect(self.ces, 15)

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 12)



class PlayerDendro (BaseRoleEvent):
    # 已测试
    role_name = "旅行者 - 草"

    cd_skill = 8
    cd_burst = 20

    ceb = "草灯莲"

    def press_skill(self):
        self.co_cooldown.skill_set()

    def press_burst(self):
        self.co_cooldown.burst_set()
        self.co_effectside.set_effect(self.ceb, 12)


class PlayerCryo (BaseRoleEvent):
    role_name = "旅行者 - 冰"



class PlayerGeo (BaseRoleEvent):
    # 已测试
    role_name = "旅行者 - 岩"
    cd_skill = 8 - 2
    cd_burst = 15

    ces = "荒星"
    ceb = "岩嶂"

    def release_skill(self):
        self.co_cooldown.skill_set()
        if self.co_effectside.exist_much(self.ces) >= 3:
            self.co_effectside.del_effect(self.ces, 1)

        self.co_effectside.add_effect(self.ces, 30 + 10)

    def press_burst(self):
        self.co_cooldown.burst_set()
        if self.co_effectside.exist_much(self.ces) >= 3:
            self.co_effectside.del_effect(self.ces, 1)

        self.co_effectside.set_effect(self.ceb, 15 + 5 + 1)



__all__ = [
    # "PlayerPyro",
    "PlayerHydro",
    "PlayerHydro_Constellation_2",
    "PlayerAnemo",
    "PlayerElectro",
    "PlayerDendro",
    # "PlayerCryo",
    "PlayerGeo"
    ]
