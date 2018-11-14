string = str(input())

sepList = string.split("-")

newList = []

for word in sepList:
    newList.append(word[0])


finalList = ''
finalList = finalList.join(newList)

print(finalList)
