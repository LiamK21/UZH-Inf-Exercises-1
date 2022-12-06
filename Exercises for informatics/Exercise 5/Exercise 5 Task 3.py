dataset = ["Hellohello", "hello"]

def reverse_index(dataset):
    index_dictionary = {}
    keys = []
    values = []
    data_list = []
    for i, k in enumerate(dataset):
        data_list.append(k.lower())
        keys.extend(k.split(" "))
    for k in keys:
        values.append(k.lower())
    keys = values
    values = []
    for m in range(len(keys)):
        for i, k in enumerate(keys):
            if i == keys.index(k):
                pass
            else:
                del (keys[i])
    for z in keys:
        values.append([])
    for i, k in enumerate(data_list):
        for g, v in enumerate(keys):
            if v in k:
                values[g].append(i)
    for i in range(len(keys)):
        index_dictionary[keys[i]] = values[i]
    print(keys)
    print(data_list)
    print(values)
    return index_dictionary


print(reverse_index(dataset))
