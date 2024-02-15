# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# local
import env
from constants import effect_site_mode as esm
from library.configuration import *


class LocalConfig (Configuration):
    window_cooldown_site_x:   IntVariable
    window_cooldown_site_y:   IntVariable
    window_cooldown_interval: IntVariable

    window_effectside_site_x:   IntVariable
    window_effectside_site_y:   IntVariable
    window_effectside_baseline: IntVariable
    window_effectside_mode:     StrVariable
    window_effectside_amount:   IntVariable

    window_clock_oversee: IntVariable

    role_1: StrVariable
    role_2: StrVariable
    role_3: StrVariable
    role_4: StrVariable

    action_key_role_1: StrVariable
    action_key_role_2: StrVariable
    action_key_role_3: StrVariable
    action_key_role_4: StrVariable
    action_key_attack: StrVariable
    action_key_skill:  StrVariable
    action_key_burst:  StrVariable
    action_key_sprint: StrVariable
    action_key_aiming: StrVariable
    action_key_jump:   StrVariable
    action_key_reset:  StrVariable

    action_key_role_1_sec: StrVariable
    action_key_role_2_sec: StrVariable
    action_key_role_3_sec: StrVariable
    action_key_role_4_sec: StrVariable
    action_key_attack_sec: StrVariable
    action_key_skill_sec:  StrVariable
    action_key_burst_sec:  StrVariable
    action_key_sprint_sec: StrVariable
    action_key_aiming_sec: StrVariable
    action_key_jump_sec:   StrVariable
    action_key_reset_sec:  StrVariable


configuration = LocalConfig()


configuration._new("window_cooldown_site_x",     int, 100)
configuration._new("window_cooldown_site_y",     int, 100)
configuration._new("window_cooldown_interval",   int, 97,           range(20, 200+1))

configuration._new("window_effectside_site_x",   int, 400)
configuration._new("window_effectside_site_y",   int, 100)
configuration._new("window_effectside_baseline", int, 0,            (0, 1))
configuration._new("window_effectside_mode",     str, esm.VERTICAL, esm.ALLMODES)
configuration._new("window_effectside_amount",   int, 8,            range(1, 21))

configuration._new("window_clock_oversee",       int, 0,            (0, 1))

configuration._new("role_1", str, "")
configuration._new("role_2", str, "")
configuration._new("role_3", str, "")
configuration._new("role_4", str, "")

configuration._new("action_key_role_1", str, "1")
configuration._new("action_key_role_2", str, "2")
configuration._new("action_key_role_3", str, "3")
configuration._new("action_key_role_4", str, "4")
configuration._new("action_key_attack", str, "Button.left")
configuration._new("action_key_skill",  str, "e")
configuration._new("action_key_burst",  str, "q")
configuration._new("action_key_sprint", str, "Key.shift")
configuration._new("action_key_aiming", str, "r")
configuration._new("action_key_jump",   str, "Key.space")
configuration._new("action_key_reset",  str, "110")

configuration._new("action_key_role_1_sec", str, "ABS_HAT0Y_UP")
configuration._new("action_key_role_2_sec", str, "ABS_HAT0X_RIGHT")
configuration._new("action_key_role_3_sec", str, "ABS_HAT0X_LEFT")
configuration._new("action_key_role_4_sec", str, "ABS_HAT0Y_DOWN")
configuration._new("action_key_attack_sec", str, "BTN_EAST")
configuration._new("action_key_skill_sec",  str, "ABS_RZ")
configuration._new("action_key_burst_sec",  str, "BTN_NORTH")
configuration._new("action_key_sprint_sec", str, "BTN_TR")
configuration._new("action_key_aiming_sec", str, "ABS_Z")
configuration._new("action_key_jump_sec",   str, "BTN_SOUTH")
configuration._new("action_key_reset_sec",  str, "")


try:
    configuration._load_json(env.cwd.assets.configuration)

except Exception as _:
    ...
