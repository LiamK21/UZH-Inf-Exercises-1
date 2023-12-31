from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        try:
            side_length = float(side_length)
        except:
            raise Warning("Input must be a number")
        if not side_length > 0:
            raise Warning("Numbers must be positive")
        super().__init__(color, filled)
        self.__side_length = side_length

    def get_side_length(self):
        copy = self.__side_length
        return copy

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        area = 6 * pow(self.__side_length, 2)
        return round(area, 2)

    def get_volume(self):
        volume = pow(self.__side_length, 3)
        return round(volume, 2)
