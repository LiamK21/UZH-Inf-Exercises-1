h = 10


def build_string_pyramid():
    s = ""
    for pyramid_height in range(1, h+1):
        for pyramid_numbers in range(1, pyramid_height+1):
                s += str(pyramid_numbers)
                if pyramid_height == pyramid_numbers:
                    pass
                else:
                    s += "*"
        s += "\n"
    for pyramid_height2 in range(1, h):
        for pyramid_numbers2 in range(1, h):
            s += str(pyramid_numbers2)
            if pyramid_numbers2 == h - pyramid_height2:
                break
            s += "*"
        s += "\n"
    return s


print(build_string_pyramid())
