from exchange_rates import EXCHANGE_RATES


def convert(amount, from_currency, to_currency):
    if (isinstance(amount, float) or isinstance(amount, int)) and amount > 0:
        if isinstance(from_currency, str):
            if from_currency in EXCHANGE_RATES.keys() and to_currency in EXCHANGE_RATES.keys():
                if to_currency in EXCHANGE_RATES[from_currency]:
                    amount = amount * EXCHANGE_RATES[from_currency][to_currency]
                    print(amount)
                    return amount
            else:
                raise Warning("Currency not available")

                if to_currency in EXCHANGE_RATES.keys():
                    if from_currency in EXCHANGE_RATES[to_currency]:
                        amount = amount / EXCHANGE_RATES[to_currency][from_currency]
                        print(amount)
                        return amount
        else:
            raise Warning("Currency is not a string")
    else:
        raise Warning("amount input must be a positive number")
