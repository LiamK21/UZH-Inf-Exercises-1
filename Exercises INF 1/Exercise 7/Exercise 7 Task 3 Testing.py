from unittest import TestCase
from Exercise7Task3 import max_profit


class MaxProfitTest(TestCase):


    def test_int_number(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5]))

    def test_1_numbers(self):
        self.assertEqual(0, max_profit([1]))

    def test_negative_numbers(self):
        self.assertEqual("Invalid Prices", max_profit([-1, 2, 3]))

    def test_non_input_list(self):
        self.assertEqual("Invalid Input Type", max_profit(1))

    def test_float_numbers(self):
        self.assertEqual("Invalid Data Type within List", max_profit([1, 2.4, 3, 4]))

    def test_no_profit(self):
        self.assertEqual(0, max_profit([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertEqual("Empty Price List", max_profit([]))