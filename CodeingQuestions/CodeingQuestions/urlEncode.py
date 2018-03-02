def urlEncode(str):
    if len(str) < 1:
        return

    charIndex = 0
    for index in reversed(range(len(str))):
        if len(str[index]) <= 0:
            continue
        else:
            charIndex = index
            break

    index = len(str) - 1
    while(index >= 0):
        if str[charIndex] == " ":
            charIndex -= 1
            str[index] ="0"
            str[index - 1] ="2"
            str[index - 2] ="%"
            index -= 3
        else:
            str[index] = str[charIndex]
            charIndex -= 1
            index -= 1

    return str
                        




print("hi this", urlEncode(['h', 'i' , ' ', 't', 'h', 'i', 's', '', '']))
print("hi this is sridev", urlEncode(['h', 'i' , ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 's', 'r', 'i', 'd', 'e', 'v', '', '', '', '', '', '']))
print("hi this", urlEncode(['h', 'i' , ' ', 't', 'h', 'i', 's', '', '']))
print("hi this ", urlEncode(['h', 'i' , ' ', 't', 'h', 'i', 's', ' ', '', '', '', '']))
print("  hi this", urlEncode([' ', ' ', 'h', 'i' , ' ', 't', 'h', 'i', 's', '', '', '', '', '', '']))