# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import core
import module
import window
from constants import *
from constants import effect_site_mode as esm
from library.anchor_point import AnchorPoint


COLOR = "white"


class EffectSideWindow (object):
    def __init__(self, window: ttkbootstrap.Toplevel):
        self.window = window
        self.toggle = "odd"
        self.mode = core.configuration.window_effectside_mode
        self.amount = core.configuration.window_effectside_amount
        self.baseline = core.configuration.window_effectside_baseline
        self.anchorpoint: AnchorPoint
        self.initial()


    def update_configuration(self, *_):
        core.configuration.window_effectside_site_x.set(window.window_effectside.winfo_x())
        core.configuration.window_effectside_site_y.set(window.window_effectside.winfo_y())


    def initial(self):
        self.canvas = ttkbootstrap.Canvas(self.window, background=TRANSPARENTCOLOR)
        self.canvas.pack(fill="both", expand=True)

        self.set_amount(self.amount)
        window.method.motion_window_by_canvas(self.window, self.canvas, "motion", self.update_configuration)


    def _kwds_base(self) -> dict:
        result = {
            "fill": TRANSPARENTCOLOR,
            "width": 0,
            "outline": "",
            "tags": "base"
        }
        return result
    

    def _kwds_baseline(self) -> dict:
        result = {
            "fill": COLOR,
            "width": 0,
            "outline": "",
            "tags": "baseline"
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
        serial_count = {x: 0 for x in range(4)}
        for index, unit in enumerate(module.effectside.get()):
            serial = unit.serial - 1

            match self.mode:
                case esm.VERTICAL:
                    site = self.anchorpoint.coordinates(index)

                case esm.HORIZONTAL:
                    site = self.anchorpoint.coordinates(index)

                case esm.SERIAL_VERTICAL:
                    site = self.anchorpoint.coordinates(serial, serial_count[serial])

                case esm.SERUAL_HORIZONTAL:
                    site = self.anchorpoint.coordinates(serial, serial_count[serial])

                case _:
                    site = self.anchorpoint.coordinates(index)

            serial_count[serial] += 1

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


    def set_amount(self, value: int = 8, update: bool = True):
        if not isinstance(value, int):
            TypeError

        if value < 1:
            ValueError

        self.amount = value
        if update: self.set_mode()


    def set_mode(self, mode: str = ..., amount: int = ...):
        mode = mode if mode in esm.ALLMODES else self.mode
        self.mode = mode

        if isinstance(amount, int): self.set_amount(amount, False)
        amount = self.amount

        width  = 0
        height = 0

        match mode:
            case esm.VERTICAL :
                width  = 10 + 230
                height = 10 + 60  * amount
                self.anchorpoint = AnchorPoint((10, 10), (0, 60))

            case esm.HORIZONTAL:
                width  = 10 + 230 * amount
                height = 10 + 60
                self.anchorpoint = AnchorPoint((10, 10), (230, 0))

            case esm.SERIAL_VERTICAL:
                width  = 10 + 230 * 4
                height = 10 + 60  * amount
                self.anchorpoint = AnchorPoint((10, 10), (230, 0), (0, 60))

            case esm.SERUAL_HORIZONTAL:
                width  = 10 + 230 * amount
                height = 10 + 60  * 4
                self.anchorpoint = AnchorPoint((10, 10), (0, 60), (230, 0))

            case _:
                width  = 10 + 230
                height = 10 + 60
                self.anchorpoint = AnchorPoint((10, 10), (60, 230), (60, 230))

        self.window.geometry(f"{width}x{height}")
        self.canvas.delete("base")
        self.canvas.delete("baseline")
        self.canvas.create_rectangle(0, 0, width, height, **self._kwds_base())
        self.set_baseline(self.baseline)


    def set_baseline(self, value: bool = False):
        self.baseline = value

        if value:
            points = []

            match self.mode:
                case esm.VERTICAL:
                    site = self.anchorpoint.coordinates()
                    points.append((site.x, 0, site.x+220, 2))

                case esm.HORIZONTAL:
                    site = self.anchorpoint.coordinates()
                    points.append((0, site.y, 2, site.y+50))

                case esm.SERIAL_VERTICAL:
                    for index in range(4):
                        site = self.anchorpoint.coordinates(index)
                        points.append((site.x, 0, site.x+220, 2))

                case esm.SERUAL_HORIZONTAL:
                    for index in range(4):
                        site = self.anchorpoint.coordinates(index)
                        points.append((0, site.y, 2, site.y+50))

                case _:
                    points = []

            for point in points:
                self.canvas.create_rectangle(*point, **self._kwds_baseline())

        else:
            self.canvas.delete("baseline")


    def moving_blocks(self, value: bool = True):
        if value:
            self.canvas.create_rectangle(0, 0, 20, 20, fill=COLOR, tags="motion")
        else:
            self.canvas.delete("motion")
