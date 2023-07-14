import random


class GameRunner(object):
    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        lst = []
        a = self.rows * self.columns
        b = 0
        while not a == b:
            x = "0x"
            for i in range(4):
                x += random.choices("0123456789ABCDEF")[0]
            lst.append(x)
            b += 1
        return lst
        # return [("0x" + "".join([random.choice("0123456789ABCDEF") for _ in range(4)])) for _ in
                # range(self.columns * self.rows)]

g = GameRunner()
print(g.generate_hex_codes())
