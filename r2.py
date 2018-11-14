n = str(input())
list = n.split()
newList = [int(i) for i in list]

print(2*newList[1] - newList[0])
