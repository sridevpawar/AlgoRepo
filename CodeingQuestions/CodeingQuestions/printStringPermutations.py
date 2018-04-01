def printStringPermutations(str):
    if len(str) == 0: return []
    if len(str) == 1: return [str]
    list = []
    for i in range(len(str)):
        a = str[i]
        b = str[:i]+str[i+1:]
        for x in printStringPermutations(b):
            list.append(a + x)

    return list



str1  = "ABC"
str2 = "ABSG"
ans1 = printStringPermutations(str1)
for a in ans1: print(a)
ans2 = printStringPermutations(str2)
for a in ans2: print(a)