def merge(a, b):
    mergelist = []
    if len(a) > len(b):
        while not len(a) == len(b):
            b.extend([b[-1]])
    if len(b) > len(a):
        while not len(a) == len(b):
            a.append(a[-1])
    for item in range(len(a)):
        mergelist.append((a[item], b[item]))
    return mergelist


print(merge([0, 1, 2],  [5, 6]))
