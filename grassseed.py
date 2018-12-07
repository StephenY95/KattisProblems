costSeed = float(input())
numLawns = int(input())

totalCost = 0

for lawn in range(0, numLawns):
    list = str(input())
    listSplit = [float(num) for num in list.split()]
    width = listSplit[0]
    length = listSplit[1]

    totalCost += width*length

totalCost = totalCost * 2
print('%.8f' % totalCost)
