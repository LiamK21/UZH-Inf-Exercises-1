from exchange_rates import EXCHANGE_RATES
from currency_converter import convert


class BankAccount:

    def __init__(self, currency="CHF"):
        if currency in EXCHANGE_RATES.keys():
            self.__currency = currency
            self.__amount = 0
        else:
            raise Warning("Currency not available")

    def correct_amount(self, amount):
        if isinstance(amount, int) or isinstance(amount, float):
            if amount > 0:
                return amount
            else:
                raise Warning("amount is negative")
        else:
            raise Warning("Amount must be a number")

    def get_currency(self):
        copy = self.__currency
        return copy

    def get_balance(self):
        copy = self.__amount
        return copy

    def deposit(self, amount, currency="CHF"):
        BankAccount.correct_amount(self, amount)
        if currency not in EXCHANGE_RATES.keys():
            raise Warning("Currency not available")
        if currency == self.__currency:
            self.__amount += amount
        else:
            x = convert(amount, currency, self.__currency)
            print(amount)
            if self.__amount < x:
                raise Warning("not enough money in the bank")
            else:
                self.__amount -= x

    def withdraw(self, amount, currency="CHF"):
        BankAccount.correct_amount(self, amount)
        if currency not in EXCHANGE_RATES.keys():
            raise Warning("Currency not available")
        if currency == self.__currency:
            if self.__amount < amount:
                raise Warning("not enough money in the bank")
            else:
                self.__amount -= amount
        else:
            amount = convert(amount, currency, self.__currency)
            if self.__amount < amount:
                raise Warning("not enough money in the bank")
            else:
                self.__amount -= amount


sut = BankAccount("CHF")
sut.deposit(150, "USD")
sut.withdraw(10.0, "EUR")
