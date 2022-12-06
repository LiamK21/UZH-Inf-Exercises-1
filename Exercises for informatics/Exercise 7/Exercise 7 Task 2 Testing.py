#!/usr/bin/env python3
from unittest import TestCase
from Exercise7Task2 import convert_roman_to_int

class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)

    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    def test_simple_subtractive(self):
        self._assert("IX", 9)

    def test_longer_additive1(self):
        self._assert("VIII", 8)

    def  test_not_valid(self):
        self.assertRaises(KeyError)

    def test_subtractive_and_additive(self):
        self._assert("XIV", 14)

    def test_double_5(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VV")

    def test_double_50(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("LL")

    def test_double_500(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("DD")

    def test_double_subtractive_additive1(self):
        self._assert("CDXC", 490)

    def test_double_subtractive_additive2(self):
        self._assert("XLIX", 49)

    def test_any_amount_M1(self):
        self._assert("MMMMMI", 5001)

    def test_any_amount_M2(self):
        self._assert("MMMMI", 4001)

    def test_amount_4_of_I(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IIII")

    def test_not_using_subtractive(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VIIII")

    def test_amount_4_of_X(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("XXXX")

    def test_amount_4_of_C(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("CCCC")

    def test_incorrect_format1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IIMX")

    def test_incorrect_format2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IVII")

    def test_pattern_X(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IXIX")

    def test_pattern_V(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IVIV")

    def test_pattern_M(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IMIM")
