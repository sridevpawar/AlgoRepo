import collections
def noRepeatedChar(str):
    letter = collections.Counter(str)
    unique = 0
    words = [word for word, count in letter.most_common(len(letter))]
    for x in words:
        if letter[x] == 1:
            unique += 1
            del letter[x]

    while len(letter) > 1:
        words = [word for word, count in letter.most_common(len(letter))]
        i = len(letter) - 1
        if letter[words[0]] - letter[words[i]] >= 0:
            x = letter[words[i]]
            del letter[words[i]]
            letter[words[0]] -= x

    if len(letter) == 0:
        return 1
    elif len(letter) == 1 and unique > 0:
        letter[letter.most_common(1)[0][0]] -= unique
        
    if letter[letter.most_common(1)[0][0]] <= 1:
            return 1
    else:
        return 0
        

def noRepeatedCharSimple(str):
    letter = collections.Counter(str)
    nonF = 0
    words = [word for word, count in letter.most_common(len(letter))]
    for x in words[1:]:
        nonF += letter[x]

    if letter[words[0]] > nonF + 1:
        return 0
    else:
        return 1
        

str = "axiqenxohssbtwwwwwwwwwwwwwww"
print(noRepeatedCharSimple(str))