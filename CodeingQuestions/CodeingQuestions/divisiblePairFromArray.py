def divisiblePairFromArray(arr, k):
    if sum(arr) % k != 0: return False
    for x in range(1, 100):
        if k * x > sum(arr): return False
        while len(arr) > 0:
            res = checkPairsExisit([arr[0]] + arr[1:], k * x)
            if len(arr) == len(res): break
            arr = res
        if len(arr) == 0: break

    return True if len(arr) == 0 else False


def checkPairsExisit(arr, k):
    if k == 0: return True
    if len(arr) == 0: return False
    for i in range(len(arr)):
        if arr[i] > k: continue
        res = checkPairsExisit(arr[:i] + arr[i + 1:], k - arr[i])
        if res == True:
            return arr[:i] + arr[i + 1:]
        elif len(res) < len(arr) - 1:
            return res

    return arr




arr = [22,7,3,11,34,8,32,3]
print(divisiblePairFromArray(arr, 10))