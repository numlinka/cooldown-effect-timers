# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# local
import env
from library.configuration import *


class LocalConfig (Configuration):
    window_cooldown_site_x: IntVariable
    window_cooldown_site_y: IntVariable

    window_effectside_site_x: IntVariable
    window_effectside_site_y: IntVariable
    window_effectside_interval: IntVariable

    role_1: StrVariable
    role_2: StrVariable
    role_3: StrVariable
    role_4: StrVariable



configuration = LocalConfig()


configuration._new("window_cooldown_site_x", int, 100)
configuration._new("window_cooldown_site_y", int, 100)

configuration._new("window_effectside_site_x", int, 400)
configuration._new("window_effectside_site_y", int, 100)
configuration._new("window_effectside_interval", int, 97, range(20, 200+1))

configuration._new("role_1", str, "")
configuration._new("role_2", str, "")
configuration._new("role_3", str, "")
configuration._new("role_4", str, "")

try:
    configuration._load_json(env.filepath.sldata.configuration)

except Exception as _:
    ...
