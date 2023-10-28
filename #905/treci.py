def proveri(k, lista):
    if k == 2:
        for l in lista:
            if l % 2 == 0:
                return 0
        return 1
    
    mini = 0
    if k == 3:
        for l in lista:
            if l % 3 == 0:
                return 0
            else:
                minip = l % 3
                if (minip > mini):
                    mini = minip
        if mini == 1:
            return 2
        else:
            return 1
    
    sadva = 0
    if k == 4:
        for l in lista:
            if l % 4 == 0:
                return 0
            elif l % 2 == 0:
                sadva += 1
                if sadva == 2:
                    return 0
            else:
                minip = l % 4
                if (minip > mini):
                    mini = minip
        if (sadva == 0):
            if (4 - mini == 1):
                return 1
            elif (len(lista) == 1):
                return 4 - mini
            else:
                return 2
        else:
            if (len(lista) == 1):
                return 2
            else:
                return 1

    if k == 5:
        for l in lista:
            if l % 5 == 0:
                return 0
            else:
                minip = l % 5
                if (minip > mini):
                    mini = minip
        return 5 - mini


n = int(input())

for _ in range(n):
    k = int(input().split(" ")[1])
    lista = [int(i) for i in input().split(" ")]

    print(proveri(k, lista))
