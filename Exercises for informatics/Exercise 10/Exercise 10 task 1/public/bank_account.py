from exchange_rates import EXCHANGE_RATES
from currency_converter import convert


class BankAccount:

    def __init__(self, currency="CHF"):
        lst = []
        for g in EXCHANGE_RATES:
            lst.append(g)
        if currency in lst:
            self.__currency = currency
            self.__amount = 0
        else:
            raise Warning("Currency not available")

    def get_currency(self):
        copy = self.__currency
        return copy

    def get_balance(self):
        copy = self.__amount
        return copy

    def deposit(self, amount, currency="CHF"):
        BankAccount.__init__(currency)
        if isinstance(amount, float) or isinstance(amount, int):
            if amount > 0:
                pass
            else:
                raise Warning("can't deposit negative amount")
        else:
            raise Warning("deposit must be a number")


    def withdraw(self, amount, currency="CHF"):
        BankAccount.__init__(currency)
        if isinstance(amount, float) or isinstance(amount, int):
            if amount > 0:
                pass
            else:
                raise Warning("can't deposit negative amount")
        else:
            raise Warning("deposit must be a number")

BankAccount()