def compress(data):
    if len(data) == 0:
        return ((), [])
    key_list = []
    value_list = []
    values = []
    for p in data[0].keys():
        key_list.append(p)
    key_list.sort()
    key_list = tuple(key_list)
    for i in range(len(data)):
        value_list.append([])
        for l in key_list:
            print(i)
            value_list[i].append(data[i][l])
    for i in range(len(value_list)):
        values.append(tuple(value_list[i]))
    return key_list, values


data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))
