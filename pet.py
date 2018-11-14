firstCandidate = str(input())
secondCandidate = str(input())
thirdCandidate = str(input())
fourthCandidate = str(input())
fifthCandidate = str(input())


def total(candidate):
    totalScoreList = [int(score) for score in candidate.split()]
    totalScore = 0
    for score in totalScoreList:
        totalScore = score+totalScore
    return(totalScore)


scores = {1: total(firstCandidate), 2: total(secondCandidate), 3: total(
    thirdCandidate), 4: total(fourthCandidate), 5: total(fifthCandidate)}


print(max(scores, key=scores.get), max(scores.values()))
