values = str(input())

list = [int(i) for i in values.split()]

numMatches = list[0]
width = list[1]
height = list[2]

hypotenuse = (width**2 + height**2)**0.5

for match in range(0, numMatches):
    matchStick = int(input())
    if (matchStick <= width) or (matchStick <= height) or (matchStick <= hypotenuse):
        print("DA")
    else:
        print("NE")
