# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import sys
import time

# site
import ttkbootstrap
from ttkbootstrap import dialogs

# local
import env
import core
from constants import *

# self
from . import method
from . import update
from ._cooldown import CoolDownWindow
from ._effect_side import EffectSideWindow
from ._interface import Interface


mainwindow = ttkbootstrap.Window()
style = ttkbootstrap.Style()
style_theme_names = style.theme_names()

window_cooldown = ttkbootstrap.Toplevel()
window_effectside = ttkbootstrap.Toplevel()


cooldown: CoolDownWindow
effectside: EffectSideWindow
interface: Interface


def initial():
    mainwindow.title(env.MAIN_TITLE)
    method.center_window_for_screen(mainwindow, 550, 330, 1)
    mainwindow.minsize(500, 300)
    method.set_window_icon(mainwindow, env.cwd.iconbitmap)
    # mainwindow.style.theme_use("darkly")
    mainwindow.style.theme_use("minty")

    window_cooldown.title("cooldown")
    window_cooldown.overrideredirect(True)
    window_cooldown.configure(highlightthickness=0)
    window_cooldown.configure(background=TRANSPARENTCOLOR)
    window_cooldown.attributes("-transparentcolor", TRANSPARENTCOLOR)
    window_cooldown.attributes("-topmost", True)
    site = f"+{core.configuration.window_cooldown_site_x}+{core.configuration.window_cooldown_site_y}"
    window_cooldown.geometry(site)

    window_effectside.title("effect")
    window_effectside.overrideredirect(True)
    window_effectside.configure(highlightthickness=0)
    window_effectside.configure(background=TRANSPARENTCOLOR)
    window_effectside.attributes("-transparentcolor", TRANSPARENTCOLOR)
    window_effectside.attributes("-topmost", True)
    site = f"+{core.configuration.window_effectside_site_x}+{core.configuration.window_effectside_site_y}"
    window_effectside.geometry(site)

    global cooldown, effectside, interface

    cooldown = CoolDownWindow(window_cooldown)
    effectside = EffectSideWindow(window_effectside)
    interface = Interface(mainwindow)

    interface.initial()
    mainwindow.after(100, final_initial)
    mainwindow.after(1000, update.check)


def final_initial():
    interface.final_initial()


mainloop = mainwindow.mainloop


__all__ = [
    "method",
    "mainwindow",
    "style_theme_names",
    "cooldown",
    "effectside",
    "interface"
]
