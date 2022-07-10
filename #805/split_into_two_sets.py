def test(lista, l1, l2):
    global uspeh
    if lista == []:
        uspeh = True
        return 0
    el = lista[0]
    if el[1] == el[0]:
        return 0
    if (el[1] not in l1 and el[0] not in l1 and el[1] not in l2 and el[0] not in l2 and l1 != l2):
        l11 = l1.copy()
        l1.append(el[0])
        l1.append(el[1])
        test(lista[1:], l1, l2)

        l2.append(el[0])
        l2.append(el[1])
        test(lista[1:], l11, l2)

    elif (el[1] not in l1 and el[0] not in l1):
        l1.append(el[0])
        l1.append(el[1])
        test(lista[1:], l1, l2)

    elif (el[1] not in l2 and el[0] not in l2):
        l2.append(el[0])
        l2.append(el[1])
        test(lista[1:], l1, l2)
    
    else:
        return 0

br_test = int(input())

for i in range(br_test):
    n = int(input())
    lista = []
    odgovori = []
    for j in range(n):
        lista.append(input().split(" "))
        uspeh = False
    test(lista, [], [])
    if uspeh:
        print("YES")
    else:
        print("NO")