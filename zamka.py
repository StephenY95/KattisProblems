min = int(input())
max = int(input())
sumDigits = int(input())

# for number in range(min, max+1):
#     digits = [int(character) for character in str(number)]
#     value = 0
#     found = False
#     for digit in digits:
#         if found is False:
#             value = value + digit
#         else:
#             break
#     if value == sumDigits:
#         found = True
#         print(value)

for number in range(max, min, -1):
    digits = [int(character) for character in str(number)]
    value = 0
    for digit in digits:
        value = value + digit
    if value == sumDigits:
        print(value)
