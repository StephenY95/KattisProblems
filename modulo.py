modulo = 0
for i in range(0, 10):
    num = int(input())
    isFloat = isinstance(num % 42, float)
    if isFloat == False:
        modulo += 1

print(modulo)
