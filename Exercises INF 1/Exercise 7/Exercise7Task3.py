def max_profit(prices):
    if type(prices) == list:
        pass
    else:
        return "Invalid Input Type"
    if len(prices) == 0:
        return "Empty Price List"

    profit = 0
    for index, i in enumerate(prices):
        p = 0
        if type(i) == int and i >= 0:
            pass
        elif i < 0:
            return "Invalid Prices"
        elif type(i) == float:
            return "Invalid Data Type within List"
        for e in prices[index+1:]:
            if p > (e - i):
                continue
            else:
                p = e - i
        if profit > p:
            pass
        else:
            profit = p
    return profit



print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([1]))
print(max_profit([5, 4, 3, 2, 1]))
print(max_profit([1, 2.4, 3, 4]))