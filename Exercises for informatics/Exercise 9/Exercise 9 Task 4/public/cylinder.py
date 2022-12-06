from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        try:
            radius = float(radius)
            height = float(height)
        except:
            raise Warning("Input must be a number")
        if not radius > 0 or not height > 0:
            raise Warning("Numbers must be positive")
        super().__init__(color, filled)
        self.__pi = 3.14
        self.__radius = radius
        self.__height = height

    def get_radius(self):
        copy = self.__radius
        return copy

    def get_height(self):
        copy = self.__height
        return copy

    def get_area(self):
        area = 2 * self.__pi * pow(self.__radius, 2) + 2 * self.__pi * self.__radius * self.__height
        return round(area, 2)

    def get_volume(self):
        volume = self.__pi * pow(self.__radius, 2) * self.__height
        return round(volume, 2)
