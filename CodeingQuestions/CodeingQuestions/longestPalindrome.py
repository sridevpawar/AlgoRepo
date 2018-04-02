def longestPalindrome(str):
    if str == str[::-1]: return str
    for l in reversed(range(2, len(str))):
        start = 0
        end = l - 1
        for i in range(len(str) - l + 1):
            temp = str[start + i:end + i + 1]
            if temp == temp[::-1]:
                return temp



a=int(input())
while a > 0:
    str = input()
    temp = longestPalindrome(str)
    if temp == None: temp = str[0]
    print(temp)
    a -= 1