def longestSubStringWithUniqueChar(str):
    maxCount = 0
    count = 0
    index = 0
    freq = [False for _ in range(256)]
    str.lower()
    while index < len(str):
        if freq[ord(str[index])] == False:
            freq[ord(str[index])] = True
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
            freq = [False for _ in range(256)]
            i = index - 1
            while str[i] != str[index]:
                i -= 1

            index = i

        index += 1

    maxCount = max(maxCount, count)
    return maxCount



str1 = "aewergrththy"
print(longestSubStringWithUniqueChar(str1))