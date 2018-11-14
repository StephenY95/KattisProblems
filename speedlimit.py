numRecords = int(input())

tracker = 0
numMiles = 0
prevMiles = 0

while numRecords != -1:
    for record in range(0, numRecords):
        recorded = str(input())
        recordedList = [int(item) for item in recorded.split()]
        time = recordedList[1] - prevMiles
        numMiles = numMiles + (recordedList[0] * time)
        prevMiles = recordedList[1]
    print(numMiles, " miles")
    numRecords = int(input())
    tracker = prevMiles = numMiles = 0
