string = str(input())
newString = string.split()


newString = [int(i) for i in newString]

x = newString[0]
y = newString[1]
n = newString[2]


for i in range(1, n+1):
    if (i % x == 0) and(i % y == 0):
        print("FizzBuzz")
    elif (i % x == 0):
        print("Fizz")
    elif (i % y == 0):
        print("Buzz")
    else:
        print(i)
