plain_text = "abcdefghijklmnopqrstuvwxyz"
shift_by = 33
print(ord("a"))


def rot_n():
    encoded = ""
    for e in plain_text:
        if e.isalpha():
            number_ASCII_original = ord(e)
            shifter = shift_by % 26
            number_ASCII_new = shifter + number_ASCII_original
            if ord("A") <= number_ASCII_original <= ord("Z"):
                if number_ASCII_new > ord("Z"):
                    number_ASCII_new -= 26
                elif number_ASCII_new < ord("A"):
                    number_ASCII_new += 26
            elif ord("a") <= number_ASCII_original <= ord("z"):
                if number_ASCII_new > ord("z"):
                    number_ASCII_new -= 26
                elif number_ASCII_new < ord("a"):
                    number_ASCII_new += 26
        else:
            number_ASCII_new = ord(e)
        encoded += chr(number_ASCII_new)
    return encoded


print(rot_n())
