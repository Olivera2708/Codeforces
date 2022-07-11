def sredi(niz):
    prosli = set()
    br = 0
    for el in niz:
        if el not in prosli:
            br += 1
            prosli.add(el)
    if (len(niz) - br) % 2 != 0:
        return br-1
    return br


test = int(input())

for i in range(test):
    n = int(input())
    niz = input().split(" ")
    print(sredi(niz))