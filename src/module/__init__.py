# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# self
from . import roles
from ._clock import Clock
from ._role_serial import RoleSerial
from ._cool_down import CoolDown
from ._effect_side import EffectSide
from ._incident import Incident
from ._handle import Handle

_clock = Clock()
roleserial = RoleSerial()
cooldown = CoolDown()
effectside = EffectSide()
incident = Incident()
handle = Handle()


def initial():
    roles.initial()
    _clock.add_event(cooldown.clock_signal)
    _clock.add_event(effectside.clock_signal)


def start():
    _clock.start()
    cooldown.start()
    effectside.start()
    incident.start()
