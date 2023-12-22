# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

#std
import os
from typing import Any


class static (object): ...



class Directory (object):
    def __getattribute__(self, __name: str) -> Any:
        value = super().__getattribute__(__name)

        if isinstance(value, str) and not os.path.isdir(value):
            try:
                os.makedirs(value)

            except Exception:
                ...

        return value


__all__ = [
    "static",
    "Directory"
]
