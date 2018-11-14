numMBs = int(input())
numMonths = int(input())

months = []
megabytes = numMBs

for month in range(0, numMonths):
    mb = int(input())
    excess = numMBs-mb
    megabytes = megabytes + excess

print(megabytes)
