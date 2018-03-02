
print("helooooooo")
def repeatCharWithIndex(str):
    if len(str) > 26 or len(str) < 1:
        return False
    
    checker = [False for i in range(128)]
    for char in str:
        achiiValue = ord(char)
        if checker[achiiValue]:
            return False
        else:
            checker[achiiValue] = True

    return True


print("34343: ", repeatCharWithIndex("34343"))
print("a: ", repeatCharWithIndex("a"))
print("abcdefghijklmnopqrstuvwxyz: ", repeatCharWithIndex("abcdefghijklmnopqrstuvwxyz"))
print("abcdefghijklmnaopqrstuvwxyz: ", repeatCharWithIndex("abcdefghijklmnaopqrstuvwxyz"))
print("empty string: ", repeatCharWithIndex(""))
print("long string: ", repeatCharWithIndex("kldsjflkjdlkfjlkjdslkfjlkdsjlfkjlsdfhlfkdhjfhdgfdgygueguufyueyfueufguhgduygfgyugsidfguyg7yfdyheuidfhygwe7ygfd8ygew8yg8yfewghe7ygfy7wgryugfeigewyug"))