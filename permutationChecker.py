def permutationChecker(str1, str2): 
    if len(str1) != len(str2) or len(str1) < 1 or len(str2) < 1:
        return False
    
    checker = [0 for i in range(128)]
    for char in str1:
        achiiValue = ord(char)
        checker[achiiValue] += 1

    for char in str2:
        achiiValue = ord(char)
        if checker[achiiValue] == 0:
            return False
        else:
            checker[achiiValue] -= 1


    return checker == [0 for i in range(128)]


print("{34343} {33344}T: ", permutationChecker("34343", "33344"))
print("{a} {b}F: ", permutationChecker("a", "b"))
print("{abcdefghijklmnopqrstuvwxyz} {abcdefghijklmnopqrstuvwxyzf}F: ", permutationChecker("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzf"))
print("{abcdefghijklmnopqrstuvwxyz} {fghstuabmnocdevwxyzijklpqr}T: ", permutationChecker("abcdefghijklmnopqrstuvwxyz", "fghstuabmnocdevwxyzijklpqr"))
print("{abcdefghijklmnaopqrstuvwxyz} {abcdefghijklmnopqrstuvwxyz}F: ", permutationChecker("abcdefghijklmnaopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))
print("empty stringF: ", permutationChecker("", "df"))
print("long stringT: ", permutationChecker("kldsjflkjdlkfjlkjdslkfjlkdsjlfkjlsdfhlfkdhjfhdgfdgygueguufyueyfueufguhgduygfgyugsidfguyg7yfdyheuidfhygwe7ygfd8ygew8yg8yfewghe7ygfy7wgryugfeigewyug", "kldsjflkjdlkfjlkjdslkfjlkdsjlfkjlsdfhlfkdhjfhdgfdgygueguufyueyfueufguhgduygfgyugsidfguyg7yfdyheuidfhygwe7ygfd8ygew8yg8yfewghe7ygfy7wgryugfeigewyug"))