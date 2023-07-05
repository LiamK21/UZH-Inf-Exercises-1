from exchange_rates import EXCHANGE_RATES


def convert(amount, from_currency, to_currency):
    if type(amount) == int or type(amount) == float:
        if amount > 0:
            if isinstance(from_currency, str):
                if from_currency in EXCHANGE_RATES.keys() and to_currency in EXCHANGE_RATES.keys():
                    if to_currency in EXCHANGE_RATES[from_currency]:
                        amount = amount * EXCHANGE_RATES[from_currency][to_currency]
                        return amount
                    elif from_currency in EXCHANGE_RATES[to_currency]:
                        amount = amount / EXCHANGE_RATES[to_currency][from_currency]
                        return amount
                else:
                    raise Warning("Currency not available")
            else:
                raise Warning("Currency is not a string")
        else:
            raise Warning("amount is negative")
    else:
        raise Warning("amount input must be a positive number")

c = convert(150, "USD", "CHF")
print(c)
