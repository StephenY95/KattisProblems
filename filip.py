numbers = str(input())

listNums = [int(number) for number in numbers.split()]
finalList = []

for number in listNums:
    newNum = int(str(number)[::-1])
    finalList.append(newNum)

if finalList[0] > finalList[1]:
    print(finalList[0])
else:
    print(finalList[1])
