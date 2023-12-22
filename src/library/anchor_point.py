# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

class Coordinates (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y



class AnchorPoint (object):
    def __init__(self,
                 origin_coordinates: tuple[int] = (0, 0),
                 base_offset: tuple[int] = (0, 10),
                 unit_offset: tuple[int] = (0, 0)):

        self.origin_coordinates = 0, 0
        self.base_offset = 0, 10
        self.unit_offset = 0, 0

        self.set_origin_coordinates(*origin_coordinates)
        self.set_base_offset(*base_offset)
        self.set_unit_offset(*unit_offset)


    def set_origin_coordinates(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            return TypeError

        self.origin_coordinates = x, y


    def set_base_offset(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            return TypeError

        self.base_offset = x, y


    def set_unit_offset(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            return TypeError

        self.unit_offset = x, y


    def coordinates(self, offset_unit: int = 0):
        orx, ory = self.origin_coordinates
        ox1, oy1 = self.base_offset
        ox2, oy2 = self.unit_offset

        rux = orx + (ox1 + ox2) * offset_unit
        ruy = ory + (oy1 + oy2) * offset_unit

        return Coordinates(rux, ruy)