def combinationSum(arr, target):
    res = []
    for i in range(len(arr)):
        if arr[i] < target:
            temp = combinationSum(arr[i + 1:], target - arr[i])
            for t in temp:
                res.append([arr[i]] + t)
        elif arr[i] == target:
            res.append([arr[i]])

    return res





arr = [10,1,2,7,6,1,5]
print(combinationSum(sorted(arr), 8))