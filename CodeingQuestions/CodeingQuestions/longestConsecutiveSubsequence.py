def longestConsecutiveSubsequence(arr):
    count = 1
    num = arr[0]
    maxCount = 1
    for i in range(1, len(arr)):
        if arr[i] == num + 1 or num - 1 == arr[i]:
            count += 1
            num = arr[i]
        else:
            num = arr[i]
            maxCount = max(maxCount, count)
            count = 1

    return max(maxCount, count)


arr = [165, 96, 9, 53, 105, 70, 24, 124, 169, 33, 147, 127, 131, 49, 63, 78, 110, 157, 58, 136, 175, 85, 158, 103, 65, 47, 129, 41, 193, 94, 137, 154, 99, 194, 76, 118, 145, 109, 18, 25, 192, 123, 121, 139, 151, 191]
print(longestConsecutiveSubsequence(sorted(arr)))