from numpy import sum, array

test = int(input())

for i in range(test):
    num = input().split(" ")
    num = [int(n) for n in num]

    n = num[0]
    m = num[1]

    numbers = []
    for j in range(n):
        inp = input().split(" ")
        inp = array([int(inpu) for inpu in inp])
        numbers.append(inp)

    res = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res += sum(array([abs(numbers[i][k] - numbers[j][k]) for k in range(m)]))

    print(res)