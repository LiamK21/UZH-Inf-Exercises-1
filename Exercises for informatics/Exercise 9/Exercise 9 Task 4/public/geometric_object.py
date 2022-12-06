from abc import ABC, abstractmethod


class GeometricObject(ABC):

    def __init__(self, color, filled):
        if not isinstance(color, str) and not isinstance(filled, bool):
            raise Warning("Wrong input")
        self._color = color
        self.__filled = filled


    def get_color(self):
        copy = self._color
        return copy


    def set_color(self, color):
        if not isinstance(color, str):
            raise Warning("Input is not a color!")
        self._color = color

    def get_filled(self):
        copy = self.__filled
        return copy

    def set_filled(self, filled):
        if not isinstance(filled, bool):
            raise Warning("Input must be True or False")
        self.__filled = filled

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass
