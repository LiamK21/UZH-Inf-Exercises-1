def invert(d):
    nv = []
    nk = []
    inverted_d = {}
    for i, j in d.items():
        nv.append([i])
        nk.append(j)
    for index, key in enumerate(nk):
        if index == nk.index(key):
            pass
        else:
            nv[nk.index(key)].append(nv[index])
            del(nv[index])
            del(nk[index])
    for i in nv:
        i.sort()
    for i in range(len(nk)):
        inverted_d[nk[i]] = nv[i]
    return inverted_d

print(invert({"a": 1, "b": 1, "c": 3, "d": 1}))