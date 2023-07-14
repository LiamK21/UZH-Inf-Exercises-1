#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, float) or not isinstance(gas_per_100km, float):
            raise Warning
        if (gas_capacity or gas_per_100km) < 0:
            raise Warning
        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__actual_gas = gas_capacity

    def fuel(self, f):
        if not type(f) == float or f < 0:
            raise Warning("Can't put in a negative number")
        if (self.__actual_gas + f) > self.__gas_capacity:
            raise Warning
        else:
            self.__actual_gas += f

    def get_gas_tank_status(self):
        return (self.__actual_gas, self.__gas_capacity)

    def get_remaining_range(self):
        return (self.__actual_gas / self.__gas_per_100km) * 100

    def drive(self, dist):
        if isinstance(dist, float) or isinstance(dist, int):
            pass
        else:
            raise Warning("Input must be a number")
        if not dist >= 0:
            raise Warning("Input must be a natural number")
        dist = float(dist)
        verbrauch = (dist / 100) * self.__gas_per_100km
        if self.__actual_gas - verbrauch < 0:
            raise Warning("Fuel is depleted")
        self.__actual_gas -= verbrauch


c = CombustionCar(40.0, 8.0)
c.get_remaining_range() # 500
c.drive(500.0)
print(c.get_gas_tank_status())
print(c.get_remaining_range())# (38.0, 40.0)
 # fuel is depleted, Warning raised
