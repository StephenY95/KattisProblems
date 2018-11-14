n = str(input())
inputSet = n.split()
inputSet = [int(i) for i in inputSet]

set = [1, 1, 2, 2, 2, 8]

output = [0, 0, 0, 0, 0, 0]

for i in range(0, len(inputSet)):
    output[i] = set[i] - inputSet[i]

print(output)
