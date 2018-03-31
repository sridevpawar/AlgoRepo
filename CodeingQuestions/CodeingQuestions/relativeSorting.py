def relativelySort(a1, a2):
    a1.sort()
    a3 = []
    for x in a2:
        i = a1.index(x)
        while(i >= 0 and a1[i] == x):
            a3.append(x)
            a1[a1.index(x)] = -1
            i += 1

    for i in a1:
        if i != -1:
            a3.append(i)

    return a3

a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a2 = [2, 1, 8, 3]
print(relativelySort(a1, a2))
