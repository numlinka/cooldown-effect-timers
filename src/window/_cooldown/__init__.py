# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import core
import module
import window
from constants import *
from library.anchor_point import AnchorPoint


COLOR = "white"


class CoolDownWindow (object):
    def __init__(self, master: ttkbootstrap.Toplevel):
        self.master = master
        self.toggle = "odd"
        self.anchorpoint = AnchorPoint((75, 20), (0, 96))
        self.initial()


    def update_configuration(self, *_):
        core.configuration.window_cooldown_site_x.set(window.window_cooldown.winfo_x())
        core.configuration.window_cooldown_site_y.set(window.window_cooldown.winfo_y())


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


    def _kwds_rectangle(self) -> dict:
        result = {
            "fill": COLOR,
            "width": 0,
            "outline": "",
            "tags": self.toggle
        }
        return result


    def _kwds_text(self, value: int = 0) -> dict:
        result = {
            "text": "{:.1f}".format(value/10) if value != 0 else "ready",
            "fill": COLOR,
            "anchor": "e",
            "justify": "center",
            "tags": self.toggle
        }
        return result
             

    def canvas_update(self):
        for index, unit in enumerate(module.cooldown.cd2u_skills_lst):
            site = self.anchorpoint.coordinates(index)
            schedule = 100 - int(100 * unit.now / unit.max) if unit.max != 0 else 100

            points_line = (site.x, site.y, site.x+100, site.y)
            points_rectangle = (site.x, site.y-6, site.x+schedule, site.y+6)

            points_line = (site.x, site.y+4, site.x+100, site.y+4)
            points_rectangle = (site.x, site.y-5, site.x+schedule, site.y+5)


            self.canvas.create_line(*points_line, **self.__kwds_line())
            self.canvas.create_rectangle(*points_rectangle, **self._kwds_rectangle())
            self.canvas.create_text(site.x-10, site.y, **self._kwds_text(unit.now))

            if index + 1 == module.roleserial.get():
                points_polygon = (site.x+110, site.y, site.x+115, site.y-5, site.x+115, site.y+5)
                self.canvas.create_polygon(*points_polygon, **self._kwds_rectangle())

        self.toggle_update()


    def toggle_update(self):
        new_toggle = "odd" if self.toggle == "even" else "even"
        self.canvas.delete(new_toggle)
        self.toggle = new_toggle


    def set_spacing(self, value: int = 96):
        if not isinstance(value, int):
            TypeError

        if value < 20:
            ValueError

        self.anchorpoint.set_base_offset(0, value)
        # 高度(328) = 间距(96) * 3 + 20 * 2
        height = value * 3 + 40
        self.master.geometry(f"200x{height}")
        self.canvas.delete("base")
        self.canvas.create_rectangle(0, 0, 200, height, **self._kwds_base())


    def moving_blocks(self, value: bool = True):
        if value:
            self.canvas.create_rectangle(0, 0, 20, 20, fill=COLOR, tags="motion")
        else:
            self.canvas.delete("motion")
