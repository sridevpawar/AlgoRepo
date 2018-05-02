def arraySubset(arr1, arr2):
    if len(arr1) < len(arr2): return False
    master = {x for x in arr1}
    for y in arr2:
        if y not in master:
            return False

    return True



arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7]
print(arraySubset(arr1, arr2))