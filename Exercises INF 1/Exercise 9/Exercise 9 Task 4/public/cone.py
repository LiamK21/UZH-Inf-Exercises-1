from geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        try:
            radius = float(radius)
            vertical_height = float(vertical_height)
            slant_height = float(slant_height)
        except:
                raise Warning("Input must be a number")
        if not radius > 0 or not vertical_height > 0 or not slant_height > 0:
            raise Warning("Numbers must be positive")
        super().__init__(color, filled)
        self.__pi = 3.14
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height

    def get_radius(self):
        copy = self.__radius
        return copy

    def get_vertical_height(self):
        copy = self.__vertical_height
        return copy

    def get_slant_height(self):
        copy = self.__slant_height
        return copy

    def get_area(self):
        volume = self.__pi * pow(self.__radius, 2) + self.__pi * self.__radius * self.__slant_height
        return round(volume, 2)

    def get_volume(self):
        area = (1 / 3) * self.__pi * pow(self.__radius, 2) * self.__vertical_height
        return round(area, 2)
