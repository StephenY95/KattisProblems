number = int(input())
binary = []

while (number != 0):
    if number % 2 == 0:
        number = number / 2
        binary.append(0)
    elif number % 2 == 1:
        number = number // 2
        binary.append(1)
    elif number == 0:
        binary.append(0)

binary = binary[::-1]
print(binary)
