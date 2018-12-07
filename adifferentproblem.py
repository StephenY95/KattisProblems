def difference(a, b):
    if a > b:
        return(a-b)
    else:
        return(b-a)


userInput = str(input())
if userInput != "":
    input = [int(i) for i in userInput.split()]
    print(difference(input[0], input[1]))
    userInput = 1
    print(userInput)
    print(type(userInput))
    userInput = str(input())
