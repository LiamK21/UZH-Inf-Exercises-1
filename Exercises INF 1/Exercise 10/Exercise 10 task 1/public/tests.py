#!/usr/bin/env python3
from unittest import TestCase
from currency_converter import convert
from bank_account import BankAccount
# You need to add missing imports to make the test work!

class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        
    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_wrong_deposit_input(self):
        with self.assertRaises(Warning):
            sut = BankAccount("CHF")
            sut.deposit("f", "CHF")

    def test_wrong_deposit_input1(self):
        with self.assertRaises(Warning):
            sut = BankAccount("CHF")
            sut.deposit(-1, "CHF")

    def test_wrong_withdraw_input(self):
        with self.assertRaises(Warning):
            sut = BankAccount("CHF")
            sut.withdraw("f", "CHF")

    def test_wrong_withdraw_input1(self):
        with self.assertRaises(Warning):
            sut = BankAccount("CHF")
            sut.withdraw(-1, "CHF")

    def test_wrong_currency(self):
        with self.assertRaises(Warning):
            BankAccount("BTC")

    def test_wrong_currency_deposit(self):
        with self.assertRaises(Warning):
            b = BankAccount()
            b.deposit(10, "BTC", )

    def test_wrong_currency_withdraw(self):
        with self.assertRaises(Warning):
            b = BankAccount()
            b.deposit(10)
            b.withdraw(1, "USDT")

    def test_converter(self):
        with self.assertRaises(Warning):
            convert(10, "BTC", "CHF")

    def test_converter1(self):
        with self.assertRaises(Warning):
            convert(10, "CHF", "BTC")

    def test_to_much_withdrawn(self):
        with self.assertRaises(Warning):
            b = BankAccount()
            b.deposit(1)
            b.withdraw(2)

    def test_to_much_withdrawn1(self):
        with self.assertRaises(Warning):
            b = BankAccount()
            b.deposit(1)
            b.withdraw(1.5)

    def test_to_much_withdrawn2(self):
        with self.assertRaises(Warning):
            b = BankAccount()
            b.withdraw(150, "USD")




    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
