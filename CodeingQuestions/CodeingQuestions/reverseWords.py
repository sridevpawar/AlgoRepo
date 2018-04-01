def reverseWords(str):
    res = ""
    for i in reversed(range(len(str) - 1)):
        if str[i] == ".":
            res += push(i + 1, str)

    if str[0] != ".":
        res += push(0, str)

    return res[1:]

def push(index, str):
    res = "."
    while(index < len(str) and str[index] != "."):
        res += str[index]
        index += 1

    return res


str = "i.like.this.program.very.much"
print(reverseWords(str))
str2 = "pqr.mno"
print(reverseWords(str2))