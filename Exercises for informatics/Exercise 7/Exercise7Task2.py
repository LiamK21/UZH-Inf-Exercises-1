#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    num = 0
    roman_list = []
    if roman.__contains__("VV") or roman.__contains__("LL") or roman.__contains__("DD"):
        raise Warning("Invalid Input")  # Those Strings are invalid
    elif roman.__contains__("CCCC") or roman.__contains__("XXXX") or roman.__contains__("IIII"):
        raise Warning("Invalid Input")  # Those strings are invalid
    for digit in roman:
        try:
            roman_list.append(roman_single_digits[digit])
        except:  # checks if the input contains the right numerals
            raise Warning("Invalid Input")
    for i in range(len(roman_list) - 1):
        if roman_list[i] < roman_list[i + 1]:
            roman_list[i] = -roman_list[i]  # makes some of them negative
    print(roman_list)
    for v in roman_list:
        for v2 in roman_list[roman_list.index(v)+1:]:
            if v < 0:
                if v == v2:  # checks that the same number doesn't get subracted twice
                    raise Warning("Invalid Input")
                elif abs(v) <= v2 > 0:  # checks that numerals get smaller after length
                    if roman_list[roman_list.index(v2)-1] < 0:
                        continue
# allows "CDXC" to be possible; allows numbers of the same size to be subtracted by a negative number before it
                    else:
                        raise Warning("Invalid Input")
            else:
                if v < v2:  # checks that the lowest negative number gets subtracted first
                    raise Warning("Invalid Input")
    for index, numbers in enumerate(roman_list):
        num += numbers

    return num


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("IV")
e = convert_roman_to_int("CMXCIV")
print(i)
print(e)
