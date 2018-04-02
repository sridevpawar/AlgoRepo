def loggestCommonSubString(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    if len(str2) == 1:
        return str2 if str2 in str1 else None

    for l in reversed(range(1, len(str2) + 1)):
        start = 0
        end = l - 1
        for i in range(len(str2) - l + 1):
            if str2[start + i: end + i + 1] in str1:
                return str2[start + i: end + i + 1]


str1 = "abc"
str2 = "abcd"
print(loggestCommonSubString(str1, str2))