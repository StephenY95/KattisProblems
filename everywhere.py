testCases = int(input())

for trip in range(0, testCases):
    numTrips = int(input())
    cities = []
    for specificTrip in range(0, numTrips):
        city = str(input())
        if city not in cities:
            cities.append(city)
    print(len(cities))
