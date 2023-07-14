#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__type = "electric"

    def switch_to_combustion(self):
        self.__type = "combustion"

    def switch_to_electric(self):
        self.__type = "electric"

    def get_remaining_range(self):
        if self.__type == "electric":
            return ElectricCar.get_remaining_range(self)
        else:
            return CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if self.__type == "electric":
            if ElectricCar.get_remaining_range(self) > 0:
                range_electric = ElectricCar.get_remaining_range(self)
                if range_electric - dist < 0:
                    ElectricCar.drive(self, range_electric)
                    remaining_range = abs(range_electric - dist)
                    CombustionCar.drive(self, remaining_range)
                else:
                    ElectricCar.drive(self, dist)
            else:
                self.switch_to_combustion()
                self.drive(dist)
        else:
            if CombustionCar.get_remaining_range(self) > 0:
                range_combustion = CombustionCar.get_remaining_range(self)
                if range_combustion - dist < 0:
                    CombustionCar.drive(self, range_combustion)
                    remaining_range = abs(range_combustion - dist)
                    ElectricCar.drive(self, remaining_range)
                else:
                    CombustionCar.drive(self, dist)


h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
h.get_gas_tank_status() # (0.0, 40.0)
h.get_battery_status() # (20.0, 25.0)
h.get_remaining_range()
