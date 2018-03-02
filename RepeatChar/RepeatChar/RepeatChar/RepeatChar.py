def repeatChar(str):
    if len(str) > 26 or len(str) < 1:
        return False

    for charIndex, char in enumerate(str):
        for eleIndex, ele in enumerate(str):
            if charIndex == eleIndex:
                continue
            if char == ele:
                return False

    return True


print("34343: ", repeatChar("34343"))
print("a: ", repeatChar("a"))
print("abcdefghijklmnopqrstuvwxyz: ", repeatChar("abcdefghijklmnopqrstuvwxyz"))
print("abcdefghijklmnaopqrstuvwxyz: ", repeatChar("abcdefghijklmnaopqrstuvwxyz"))
print("empty string: ", repeatChar(""))
print("long string: ", repeatChar("kldsjflkjdlkfjlkjdslkfjlkdsjlfkjlsdfhlfkdhjfhdgfdgygueguufyueyfueufguhgduygfgyugsidfguyg7yfdyheuidfhygwe7ygfd8ygew8yg8yfewghe7ygfy7wgryugfeigewyug"))