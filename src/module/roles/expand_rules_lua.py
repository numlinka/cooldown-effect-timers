# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os

# site
import lupa.lua54 as lupa

# local
import env
from module._cool_down import CoolDown
from module._effect_side import EffectSide

# self
from .base import BaseRoleEvent



class LuaRoleEvent (BaseRoleEvent):
    def __init__(self, co_cooldown: CoolDown = ..., co_effectside: EffectSide = ..., luapath: str = ...):
        super().__init__(co_cooldown, co_effectside)

        self.runtime = lupa.LuaRuntime(unpack_returned_tuples=True)
        with open(luapath, "r", encoding="utf-8") as fobj: self.luacode = fobj.read()
        self.runtime.execute(self.luacode)
        self.lua = self.runtime.globals()

        self.lua.co_cooldown = co_cooldown
        self.lua.co_effectside = co_effectside

        for attrname in ["cd_skill", "cd_burst"]:
            value = getattr(self.lua, attrname)
            if isinstance(value, (int, float)):
                setattr(self, attrname, value)

        for attrname in [
            "switch_in",    "switch_out",
            "press_attack", "release_attack",
            "press_skill",  "release_skill",
            "press_burst",  "release_burst",
            "press_sprint", "release_sprint",
            "press_aiming", "release_aiming",
            "press_jump",   "release_jump",
            ]:
            value = getattr(self.lua, attrname)
            if callable(value):
                setattr(self, attrname, value)



def get_rule_lst():
    tuple = {}
    for name in os.listdir(env.cwd.assets.customize.lua):
        path = os.path.join(env.cwd.assets.customize.lua, name)
        if not os.path.isfile(path) or not name.endswith(".lua"):
            continue

        tuple[f"* {name[:-4]}"] = path

    return tuple
