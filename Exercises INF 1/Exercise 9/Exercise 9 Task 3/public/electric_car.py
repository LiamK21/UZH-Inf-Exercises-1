#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not isinstance(battery_size, float) or not isinstance(battery_range_km, float):
            raise Warning
        if (battery_size or battery_range_km) < 0:
            raise Warning
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__actual_battery = battery_size

    def charge(self, kwh):
        if not type(kwh) == float or kwh < 0:
            raise Warning("Can't put in a negative number")
        if self.__actual_battery + kwh > self.__battery_size:
            raise Warning("You stupid")
        self.__actual_battery += kwh

    def get_battery_status(self):
        return (self.__actual_battery, self.__battery_size)

    def get_remaining_range(self):
        x = self.__actual_battery / self.__battery_size
        return x * self.__battery_range_km

    def drive(self, dist):
        if isinstance(dist, float) or isinstance(dist, int):
            pass
        else:
            raise Warning("Input must be a number")
        if not dist >= 0:
            raise Warning("Input must be a natural number")
        verbrauch = self.__battery_range_km / dist
        if self.__actual_battery - verbrauch < 0:
            raise Warning("You stupid, you can't drive that long!")
        self.__actual_battery -= verbrauch

