def divisiblePairFromArray(arr, k):
    kM = {k * x for x in range(11)}
    if sum(arr) % k != 0: return False
    sorted(arr)
    checkPairsExisit(arr, k, kM)


def checkPairsExisit(arr, k, kM):
    sum = arr[len(arr)-1]
    kI = 0
    while sum >= kM[kI]:
        kI += 1

    diff = kM[kI] - sum
    if diff == 0:
        return checkPairsExisit(arr[:-1], k, kM)





arr = [91, 74, 66, 48]
print(divisiblePairFromArray(arr, 10))