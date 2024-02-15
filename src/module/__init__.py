# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# self
from . import roles
from ._clock import Clock
from ._role_serial import RoleSerial
from ._cool_down import CoolDown
from ._effect_side import EffectSide
from ._handle import Handle
from ._listen_keyboard import ListenKeyboard
from ._listen_mouse import ListenMouse
from ._listen_joystick import ListenJoystick

clock = Clock()
roleserial = RoleSerial()
cooldown = CoolDown()
effectside = EffectSide()
handle = Handle()
listen_keyboard = ListenKeyboard()
listen_mouse = ListenMouse()
listen_joystick = ListenJoystick()

def initial():
    roles.initial()
    # _clock.add_event(cooldown.clock_signal)
    # _clock.add_event(effectside.clock_signal)
    clock.add_event(cooldown._looptask)
    clock.add_event(effectside._looptask)


def start():
    clock.start()
    # cooldown.start()
    # effectside.start()
    listen_keyboard.start()
    listen_mouse.start()
    listen_joystick.start()
