n = int(input())

for i in range(0, n):
    newInput = int(input())
    if newInput % 2 == 0:
        print(newInput, " is even")
    else:
        print(newInput, " is odd")
