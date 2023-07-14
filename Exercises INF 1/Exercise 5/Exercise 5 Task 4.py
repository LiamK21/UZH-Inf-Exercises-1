def min_domino_rotations(top, bottom):
    digits = [1, 2, 3, 4, 5, 6]
    domino = 0
    amount_top = 0
    amount_bottom = 0
    last_index_number = max(range(len(top)))  # last index as a number
    for numbers in digits:
        index = 0
        while index <= last_index_number:
            if top[index] == numbers or bottom[index] == numbers:
                index += 1
            else:
                break
            if index == last_index_number:
                domino = numbers
    if domino == 0:
        return -1
    for index in range(len(top)):
        if top[index] == domino:
            amount_top += 1
        if bottom[index] == domino:
            amount_bottom += 1
    if amount_top > amount_bottom:
        return len(top) - amount_top
    elif amount_bottom > amount_top:
        return len(bottom) - amount_bottom


print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
