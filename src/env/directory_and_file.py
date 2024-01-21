# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os

# local
from library.structure import *


current_working_directory = os.getcwd()


class __cwd (DirectoryPlus):
    class sldata (DirectoryPlus):
        _self_value_ = ".sldata"
        formation = "formation"
        class customize (DirectoryPlus):
            lua = "lua"

        configuration = FilePath("configuration")

    iconbitmap = FilePath("favicon.ico")



cwd = __cwd(current_working_directory)
cwd._pass_self_ = True

abscwd = __cwd(current_working_directory)


__all__ = ["cwd", "abscwd"]
