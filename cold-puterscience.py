numTemps = int(input())
temps = str(input())

listTemps = temps.split()
newListTemps = [int(i) for i in listTemps]
underZero = 0

for i in newListTemps:
    if i < 0:
        underZero = underZero+1
print(underZero)
