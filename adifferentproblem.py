def difference(a, b):
    if a > b:
        return(a-b)
    else:
        return(b-a)


n = str(input())
while True:
    input = [int(i) for i in n.split()]
    print(difference(input[0], input[1]))
    n = (input())
