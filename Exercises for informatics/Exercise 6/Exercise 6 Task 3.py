import os


def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):                # checks if txt file exists
        return False
    names_list = []
    with open(path_reading, "r") as f:
        for index, value in enumerate(f.readlines()):
            if len(value) > 0 and index == 0:
                names_list.append(value)
            elif len(value) == 1:   # checks whether line empty or not
                names_list.append(",\n")
            elif not value.__contains__("\n"):
                if value.__contains__("; "):
                    x = value.find("; ")
                    y = value[x + 2:] + "," + value[:x]
                    names_list.append(y)
                else:
                    x = value.find(" ")
                    y = value[0: x] + "," + value[x + 1:]
                    names_list.append(y)
            elif value.__contains__("; "):            # checks the special symbols
                x = value.find("; ")
                y = value[x+2:-1] + "," + value[:x] + "\n"  # string slices the whole name
                names_list.append(y)             # without the \n and adds it at the end
            elif value.__contains__(" "):
                x = value.find(" ")
                y = value[0: x] + "," + value[x + 1:]
                names_list.append(y)
    if len(names_list) == 0:
        return open(path_writing, "w")
    elif len(names_list) == 1:
        names_list[0] = "Firstname,Lastname"
    else:
        names_list[0] = "Firstname,Lastname\n"
    with open(path_writing, "w") as p:
        for v in names_list:    # opens a new txt file, loops and adds the list elements
            p.write(v)
# if txt file has nothing written, the new file won't have anything either (l.10)


INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
