commands = int(input())

for command in range(0, commands):
    simonCommand = str(input())
    check = simonCommand.split()
    if check[0] == "Simon" and check[1] == "says":
        output = " ".join(check[2:])
        print(output)
