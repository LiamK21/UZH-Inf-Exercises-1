class MagicDrawingBoard:
    def __init__(self, x, y):
        if type(x)  == int and type(y) == int:
            pass
        else:
            raise Warning("Input must be a natural number!")
        if  x >= 1 and y >= 1:
            pass
        else:
            raise Warning("Input must be a natural number!")
        self.__x = x
        self.__y = y
        self.__world = ""
        for w in range(y):
            if w == y - 1:
                self.__world = self.__world + ("0" * x)
            else:
                self.__world = self.__world + ("0" * x) + "\n"

    def pixel(self, coordinates):
        if type(coordinates[0]) == int and type(coordinates[1]) == int:
            pass
        else:
            raise Warning("Pixel must contain natural numbers!")
        if coordinates[0] >= 1 and coordinates[1] >= 1:
            pass
        else:
            raise Warning("Pixel must contain natural numbers!")
        if coordinates[0] >= self.__x or coordinates[1] >= self.__y:
            raise Warning(f"Pixel {coordinates} out of bounds!")
        lst = []
        for i in range((len(self.__world) - self.__y + 1) // self.__x):
            lst.append(self.__world.split("\n")[i])
        lst[coordinates[1]] = lst[coordinates[1]][:coordinates[0]] + "1" + lst[coordinates[1]][coordinates[0] +1:]
        self.__world = ""
        for i in lst:
            self.__world += i + "\n"
        self.__world = self.__world[:-1]

    def rect(self, starting_coordinate, ending_coordinate):
        if type(starting_coordinate[0]) == int and type(starting_coordinate[1]) == int \
        and type(ending_coordinate[0]) == int and type(ending_coordinate[1]) == int:
            pass
        else:
            raise Warning("Rectangle coordinates must contain natural numbers!")
        if starting_coordinate[0] >= self.__x or starting_coordinate[1] >= self.__y:
            raise Warning(f"Starting coordinates {starting_coordinate} not in the world!")
        if ending_coordinate[0] > self.__x or ending_coordinate[1] > self.__y:
            raise Warning(f"Starting coordinates {ending_coordinate} not in the world!")
        if starting_coordinate[0] >= ending_coordinate[0] or starting_coordinate[1] >= ending_coordinate[1]:
            raise Warning("The rectangle is impossible!")
        lst = []
        for i in range((len(self.__world) - self.__y + 1) // self.__x):
            lst.append(self.__world.split("\n")[i])
        for line in range(starting_coordinate[1], ending_coordinate[1]):
            lst[line] = lst[line][:starting_coordinate[0]] + "1" * (ending_coordinate[0] - starting_coordinate[0]) + \
                        lst[line][ending_coordinate[0]:]
        self.__world = ""
        for i in lst:
            self.__world += i + "\n"
        self.__world = self.__world[:-1]

    def img(self):
        return self.__world

    def reset(self):
        self.__world = ""
        for w in range(self.__y):
            if w == self.__y - 1:
                self.__world = self.__world + ("0" * self.__x)
            else:
                self.__world = self.__world + ("0" * self.__x) + "\n"



if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    db.pixel((1, 1))
    db.rect((2, 2), (5, 4))
    db.reset()
    print(db.img())
