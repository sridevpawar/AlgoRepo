def formAPalindrome(str):
    if str == str[::-1]: return 0

    for i in range(len(str)):
        if str[i] == str[len(str) - 1]:
            if str[i:] == str[i:][::-1]:
                return i

    return len(str)


str1 = "babcd"
print(formAPalindrome(str1))
print(formAPalindrome(str1[::-1]))