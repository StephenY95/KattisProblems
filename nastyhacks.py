numLines = int(input())

for line in range(0, numLines):
    inputLine = str(input())
    list = [int(i) for i in inputLine.split()]
    revenueAdvertise = list[0]
    revenueNoAdvertise = list[1]
    cost = list[2]

    if revenueNoAdvertise > (revenueAdvertise + cost):
        print("advertise")
    elif revenueNoAdvertise < (revenueAdvertise + cost):
        print("do not advertise")
    else:
        print("does not matter")
