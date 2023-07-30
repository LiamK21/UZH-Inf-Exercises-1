#!/usr/bin/env python3

from unittest import TestCase
from knight import Knight
from rogue import Rogue
from mage import  Mage

class TestBattle(TestCase):

    def test_basic_attack(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_knight_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8*(3*10+0))
        self.assertEqual(expected, actual)

    def test_mage_attack(self):
        r = Rogue("Arthur", 3)
        m = Mage("Shades", 3)
        m.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(1.25*(3*10+0))
        self.assertEqual(expected, actual)

    def test_rogue_attack_mage(self):
        r = Rogue("Arthur", 3)
        m = Mage("Shades", 3)
        r.attack(m)
        actual = m.get_health()[0]
        expected = 150 - round(3*10*1.5+0)
        self.assertEqual(expected, actual)

    def test_rogue_attack_knight(self):
            r = Rogue("Arthur", 3)
            k = Knight("Shades", 3)
            r.attack(k)
            actual = k.get_health()[0]
            expected = 150 - round(3 * 10 * 0.75 + 0)
            self.assertEqual(expected, actual)

    def test_mage_attack_knight(self):
        k = Knight("Arthur", 3)
        m = Mage("Shades", 3)
        m.attack(k)
        actual = k.get_health()[0]
        expected = 150 - round(0.75*(1.25*(3*10+0)))
        self.assertEqual(expected, actual)

    def test_knight_attack_mage(self):
        k = Knight("Arthur", 3)
        m = Mage("Shades", 3)
        k.attack(m)
        actual = m.get_health()[0]
        expected = 150 - round(0.8*(1.5*(3*10+0)))
        self.assertEqual(expected, actual)

    def test_knight_lvl10_attack_mage(self):
            k = Knight("Arthur", 10)
            m = Mage("Shades", 3)
            k.attack(m)
            actual = m.get_health()[0]
            expected = 150 - round(0.8 * (1.5 * (10 * 10 + 7)))
            self.assertEqual(expected, actual)

    def test_mage_lvl10_attack_knight(self):
            k = Knight("Arthur", 3)
            m = Mage("Shades", 10)
            m.attack(k)
            actual = k.get_health()[0]
            expected = 150 - round(0.75 * (1.25 * (10 * 10 + 7)))
            self.assertEqual(expected, actual)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
