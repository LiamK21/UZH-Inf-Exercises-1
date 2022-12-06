from exchange_rates import EXCHANGE_RATES
from currency_converter import convert


class BankAccount:

    def __init__(self, currency="CHF"):
        counter = 0
        for g in EXCHANGE_RATES:
            print(g)
            print(g == currency)

    def get_currency(self):
        pass

    def get_balance(self):
        pass

    def deposit(self, amount, currency="CHF"):
        pass

    def withdraw(self, amount, currency="CHF"):
        pass

BankAccount("USD")