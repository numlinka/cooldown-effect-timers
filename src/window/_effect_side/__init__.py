# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import core
import module
import window
from constant import *
from library.anchor_point import AnchorPoint


COLOR = "white"


class EffectSideWindow (object):
    def __init__(self, master: ttkbootstrap.Toplevel):
        self.master = master
        self.toggle = "odd"
        self.anchorpoint = AnchorPoint((10, 10), (0, 60))
        self.initial()


    def update_configuration(self, *_):
        core.configuration.window_effectside_site_x.set(window.window_effectside.winfo_x())
        core.configuration.window_effectside_site_y.set(window.window_effectside.winfo_y())


    def initial(self):
        self.canvas = ttkbootstrap.Canvas(self.master, background=TRANSPARENTCOLOR)
        self.canvas.pack(fill="both", expand=True)

        self.set_spacing()
        window.method.motion_window_by_canvas(self.master, self.canvas, "motion", self.update_configuration)


    def _kwds_base(self) -> dict:
        result = {
            "fill": TRANSPARENTCOLOR,
            "width": 0,
            "outline": "",
            "tags": "base"
        }
        return result


    def __kwds_line(self) -> dict:
        result = {
            "fill": COLOR,
            "width": 0,
            "tags": self.toggle
        }
        return result


    def _kwds_rectangle_outline(self) -> dict:
        result = {
            "fill": TRANSPARENTCOLOR,
            "width": 2,
            "outline": COLOR,
            "tags": self.toggle
        }
        return result


    def _kwds_rectangle(self) -> dict:
        result = {
            "fill": COLOR,
            "width": 0,
            "outline": "",
            "tags": self.toggle
        }
        return result


    def _kwds_text(self, left_bit: bool = True) -> dict:
        result = {
            "fill": COLOR,
            "anchor": "w" if left_bit else "e",
            "justify": "center",
            "tags": self.toggle
        }
        return result


    def canvas_update(self):
        for index, unit in enumerate(module.effectside.get()):
            site = self.anchorpoint.coordinates(index)
            schedule = int(200 * unit.now / unit.max) if unit.max != 0 else 200

            points_rectangle_outline = (site.x, site.y, site.x+220, site.y+50)
            points_text_name = (site.x+10, site.y+15)
            points_text_time = (site.x+210, site.y+15)
            points_line = (site.x+10, site.y+35, site.x+210, site.y+35)
            points_rectangle = (site.x+10, site.y+30, site.x+10+schedule, site.y+40)

            points_line = (site.x+10, site.y+39, site.x+210, site.y+39)
            points_rectangle = (site.x+10, site.y+30, site.x+10+schedule, site.y+40)

            self.canvas.create_rectangle(*points_rectangle_outline, **self._kwds_rectangle_outline())
            self.canvas.create_text(*points_text_name, text=unit.name, **self._kwds_text())
            self.canvas.create_text(*points_text_time, text="{:.1f}".format(unit.now/10), **self._kwds_text(False))
            self.canvas.create_line(*points_line, **self.__kwds_line())
            self.canvas.create_rectangle(*points_rectangle, **self._kwds_rectangle())

        self.toggle_update()


    def toggle_update(self):
        new_toggle = "odd" if self.toggle == "even" else "even"
        self.canvas.delete(new_toggle)
        self.toggle = new_toggle


    def set_spacing(self, value: int = 8):
        if not isinstance(value, int):
            TypeError

        if value < 1:
            ValueError

        # 高度(490) = 间距(60) * 最大效果数量(8) + 10
        height = 60 * value + 10
        self.master.geometry(f"240x{height}")
        self.canvas.delete("base")
        self.canvas.create_rectangle(0, 0, 240, height, **self._kwds_base())


    def moving_blocks(self, value: bool = True):
        if value:
            self.canvas.create_rectangle(0, 0, 20, 20, fill=COLOR, tags="motion")
        else:
            self.canvas.delete("motion")
