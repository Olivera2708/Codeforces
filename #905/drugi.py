def proveri(nk, rec):
    recnik = {}
    for s in rec:
        if (s not in recnik):
            recnik[s] = 1
        else:
            recnik[s] += 1
    
    neparni = 0
    for v in recnik.values():
        if (v % 2 == 1):
            neparni += 1
    
    if neparni > nk[1] + 1:
        return "NO"
    else:
        return "YES"



n = int(input())

for _ in range(n):
    nk = [int(i) for i in input().split(" ")]
    rec = input()

    print(proveri(nk, rec))