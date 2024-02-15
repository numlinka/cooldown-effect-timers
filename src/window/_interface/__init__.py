# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# self
from .roles import Roles
from .display import Display
from .oversee import Oversee
from .listen import Listen
from .help import Help
from .about import About
from .customize import Customize


class Interface (object):
    def __init__(self, master: ttkbootstrap.Window):
        self.master = master

        self.notebook = ttkbootstrap.Notebook(self.master)
        self.notebook.pack(fill=BOTH, expand=True, padx=5, pady=5)


        self.frame_roles = ttkbootstrap.Frame(self.notebook)
        self.frame_display = ttkbootstrap.Frame(self.notebook)
        self.frame_oversee = ttkbootstrap.Frame(self.notebook)
        self.frame_listen = ttkbootstrap.Frame(self.notebook)
        self.frame_help = ttkbootstrap.Frame(self.notebook)
        self.frame_about = ttkbootstrap.Frame(self.notebook)
        self.frame_customize = ttkbootstrap.Frame(self.notebook)

        self.notebook.add(self.frame_roles, text="角色")
        self.notebook.add(self.frame_display, text="悬浮窗")
        self.notebook.add(self.frame_oversee, text="监视器")
        self.notebook.add(self.frame_listen, text="设置")
        self.notebook.add(self.frame_help, text="帮助")
        self.notebook.add(self.frame_about, text="关于")
        self.notebook.add(self.frame_customize, text="自定义角色")

        self.roles = Roles(self.frame_roles)
        self.display = Display(self.frame_display)
        self.oversee = Oversee(self.frame_oversee)
        self.listen = Listen(self.frame_listen)
        self.help = Help(self.frame_help)
        self.about = About(self.frame_about)
        self.customize = Customize(self.frame_customize)


    def initial(self):
        self.display.initial()
        self.oversee.initial()
        self.listen.initial()


    def final_initial(self):
        self.roles.final_initial()
        self.listen.final_initial()

        # 刷新界面
        # counts = list(range(len(self.notebook.children)))
        # counts.extend(counts[::-1][1:])

        # for count in counts:
        #     self.notebook.select(count)
        #     self.master.update()
