diceInput = str(input())

diceInputList = [int(dice) for dice in diceInput.split()]

firstDice = diceInputList[0]
secondDice = diceInputList[1]

dictNums = {}

for number in range(1, firstDice+1):
    for secondNumber in range(1, secondDice+1):
        if (number+secondNumber) in dictNums:
            dictNums[number+secondNumber] += 1
        else:
            dictNums[number+secondNumber] = 1

maxValue = max(dictNums.values())

for key, value in dictNums.items():
    if value == maxValue:
        print(key)
