def evolve(world, steps):
    length_tuple = 0
    changed_world = []
    left_over_steps = steps
    if len(world) <= 3 or len(world[0]) <= 3:
        raise Warning("World is too small, 3x3 is the minimum size")
    if type(world) is not tuple:
        raise Warning("First parameter must be a tuple")
    for values in world:
        if type(values) is not str:
            raise Warning("World must be made of Strings")
        if world[0] == values:
            length_tuple = len(values)
        else:
            if values[0].__contains__("|") and values[-1].__contains__("|"):
                pass
            else:
                raise Warning("World is not closed")  # checks if the sides of the world are closed
        if length_tuple == len(values):
            pass
        else:  # checks if every tuple value has the same length
            raise Warning("World is incorrect")
        for subv in values:
            if world[0] == values or world[-1] == values:
                if not subv.__contains__("-"):  # checks if the top/bottom of the world is closed
                    raise Warning("World is not closed")
        for subv in values[1:-1]:  # iterates through tuple element without the "|"
            if world[0] == values or world[-1] == values:
                pass
            else:
                if subv.__contains__(" ") or subv.__contains__("#"):
                    pass
                else:
                    raise Warning(f"Invalid character detected: {subv}")

    if type(steps) is not int or steps < 0:
        raise Warning("Second parameter must be a positive integer")

    while left_over_steps > 0:
        if len(changed_world) == 0:
            for world_row, placeholder_changed_world in enumerate(world):
                string_row = ""
                for cell, placeholder_cell in enumerate(placeholder_changed_world):
                    counter = 0
                    if placeholder_cell.__contains__("#"):
                        counter = -1
                        for row in range(-1, 2):
                            for index in range(-1, 2):
                                if world[world_row + row][cell + index].__contains__("#"):
                                    counter += 1
                        if 2 <= counter <= 3:
                            string_row += "#"
                        else:
                            string_row += " "
                    elif placeholder_cell.__contains__(" "):
                        for row in range(-1, 2):
                            for index in range(-1, 2):
                                if world[world_row + row][cell + index].__contains__("#"):
                                    counter += 1
                        if counter == 3:
                            string_row += "#"
                        else:
                            string_row += " "
                    else:
                        string_row += placeholder_cell
                changed_world.append(string_row)
            left_over_steps -= 1
        else:
            temporary_world = changed_world[:]
            changed_world = []
            for world_row, placeholder_changed_world in enumerate(temporary_world):
                string_row = ""
                for cell, placeholder_cell in enumerate(placeholder_changed_world):
                    counter = 0
                    if placeholder_cell.__contains__("#"):
                        counter = -1
                        for row in range(-1, 2):
                            for index in range(-1, 2):
                                if temporary_world[world_row + row][cell + index].__contains__("#"):
                                    counter += 1
                        if 2 <= counter <= 3:
                            string_row += "#"
                        else:
                            string_row += " "
                    elif placeholder_cell.__contains__(" "):
                        for row in range(-1, 2):
                            for index in range(-1, 2):
                                if temporary_world[world_row + row][cell + index].__contains__("#"):
                                    counter += 1
                        if counter == 3:
                            string_row += "#"
                        else:
                            string_row += " "
                    else:
                        string_row += placeholder_cell
                changed_world.append(string_row)
            left_over_steps -= 1
    changed_world = tuple(changed_world)
    amount_hashtags = 0
    for world_row in changed_world:
        for cell in world_row:
            if cell.__contains__("#"):
                amount_hashtags += 1

    return (changed_world, amount_hashtags)


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")
