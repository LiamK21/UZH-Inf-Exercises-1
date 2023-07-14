def analyze(posts):
    list_keys = []
    list_values = []
    list_keys1 = []
    dictionary = {}
    for v in posts:
        for h in v.split(" "):
            list_keys.append(h)
    for i, v in enumerate(list_keys):
        if v.__contains__("#"):
            if v[1:2].isalpha():
                list_keys[i] = v[1:]
            else:
                list_keys[i] = 1
        else:
            list_keys[i] = 1
    for g in range(len(list_keys)):
        for v in list_keys:
            if v == 1:
                list_keys.remove(v)
    for v in list_keys:
        list_keys1.append(v)
    # list_keys1 = list_keys
    for i, v in enumerate(list_keys):
        item = v
        for g in range(len(list_keys)):
            for index, el in enumerate(list_keys):
                if item == el:
                    if not index == i:
                        del(list_keys[index])
    for i in list_keys:
        counter = 0
        for u in list_keys1:
            if i == u:
                counter += 1
        list_values.append(counter)
    for i in range(len(list_keys)):
        dictionary[list_keys[i]] = list_values[i]
    return dictionary


posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
