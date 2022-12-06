wa_nrs = ["0781111119", "0792653913", "0786432165", "0797763139", "0792793193", "0781139022", "0764320165"]


def get_possible_nrs(n):
    digits_input_nrs = []
    digits_wa_nrs = []
    valid_nrs = []
    for g in n[2:]:           #  leaves "07" out
        digits_input_nrs.append(g)

    for i in wa_nrs:    # iterate through wa_nrs
        counter = 0
        for z in i[2:]:     # iterate through the number = every digit
            digits_wa_nrs.append(z)

        for index in range(len(digits_input_nrs)):   # length of input
            if digits_wa_nrs[index] == digits_input_nrs[index]:
                pass
            else:
                if counter == 1:
                    counter += 1
                    digits_wa_nrs = []
                    break
                counter += 1
                del(digits_wa_nrs[index])
                if digits_wa_nrs[index] == digits_input_nrs[index]:  # checks if the digit at the new index position "index"  is equal
                    pass
                else:
                    counter += 1
                    digits_wa_nrs = []
                    break
        if counter <= 1:
            valid_nrs.append(i)
            digits_wa_nrs = []
    return valid_nrs


print(get_possible_nrs("076432165"))