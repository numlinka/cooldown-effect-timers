# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# self
from ._slconfig import configuration

# local
import env
import module
import window


def save_configuration():
    configuration._save_json(env.filepath.sldata.configuration)


def run():
    module.initial()
    window.initial()

    module.start()
    window.mainloop()
    save_configuration()


__all__ = ["configuration"]
