# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os
from os.path import join as __

# local
from library.structure import *


cwd = os.getcwd()


class _base (Directory):
    sldata = ".sldata"

base = _base()



class _directory (Directory):
    class __resources (str, Directory):
        ...


    sldata = __resources(".sldata")


directory = _directory()



class _filepath (static):
    class sldata (static):
        configuration = __(directory.sldata, "configuration")

    iconbitmap = "favicon.ico"


filepath  = _filepath()


__all__ = [
    "directory",
    "filepath"
]
