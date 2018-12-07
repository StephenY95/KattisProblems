inputText = str(input())

list = list(inputText)

numChars = len(list)

toggle = 0

for character in range(0, numChars-1):
    if list[character] == list[character+1] == 's':
        toggle = 1

if toggle == 0:
    print("no hiss")
else:
    print("hiss")
