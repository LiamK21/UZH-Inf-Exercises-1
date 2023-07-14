#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from character import Character


class Mage(Character):

    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))

    def _take_physical_damage(self, amount):
         super()._take_physical_damage(round(1.5*amount))
        #super(Mage, self)._take_physical_damage(round(1.5*amount))

    def _get_caused_dmg(self, other):
        # 10 * self._lvl + (self._lvl-other._lvl) = 11 * self._lvl - other._lvl
        #return round(max(1 * 1.25, 1.25 * (self._lvl * 11 - other._lvl)))
        return round(1.25 * super()._get_caused_dmg(other))