def removeAdjacentDuplicates(str):
    res = ""
    while len(str) > 0 and str != res:
        if len(res) > 0: str =  res
        res = ""
        i = 0
        while i < len(str):
            if i == len(str) - 1: 
                res += str[i]
                break
            if str[i] != str[i + 1]:
                res += str[i]
            else:
                x = str[i]
                while i + 1 < len(str) and x == str[i + 1]:
                    i += 1

            i += 1

    return res
    


str1 = "mississipie"
print(removeAdjacentDuplicates(str1))