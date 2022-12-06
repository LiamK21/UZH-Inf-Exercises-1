#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from character import Character


class Knight(Character):

    def _take_physical_damage(self, amount):
        super()._take_physical_damage(round(0.75*amount))

    def _take_magical_damage(self, amount):
        super()._take_physical_damage(round(0.75*amount))

    def _get_caused_dmg(self, other):
        # 10 * self._lvl + (self._lvl-other._lvl) = 11 * self._lvl - other._lvl
        # return round(max(1 * 0.8, 0.8 * (self._lvl * 11 - other._lvl)))
        return round(0.8 * super()._get_caused_dmg(other))
