lines = int(input())

uAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z"]
lAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
             "y", "z"]

for line in range(0, lines):
    uncheckedLine = str(input())
    newUncheckedLine = uncheckedLine.split()

    for character in newUncheckedLine:
        if character in newUncheckedLine ==
