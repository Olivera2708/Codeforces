def vrati(u, lista):
    prisutan = False
    for el in u:
        if not prisutan:
            if lista[0] == el:
                prisutan = True
        else:
            if lista[1] == el:
                return "YES"
    return "NO"

br_test = int(input())
rez = []
for i in range(br_test):
    input()
    linija1 = input().split(" ")
    n = int(linija1[0])
    k = int(linija1[1])
    u = input().split(" ")
    for i in range(k):
        print(vrati(u, input().split(" ")))
    