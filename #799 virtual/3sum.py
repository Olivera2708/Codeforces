def proveri(unos, n):
    for i in range(n-2):
        for j in range(i+1, n-1):
            broj = int(str(int(unos[i][-1]) + int(unos[j][-1]))[-1])
            for k in range(j+1, n):
                if broj < 4 and int(unos[k][-1]) == 3 - broj:
                    return True
                if int(unos[k][-1]) == 10 - broj + 3:
                    return True
    return False

test = int(input())

for i in range(test):
    n = int(input())
    unos = input().split(" ")
    nasao = proveri(unos, n)
    if nasao:
        print("YES")
    else:
        print("NO")
