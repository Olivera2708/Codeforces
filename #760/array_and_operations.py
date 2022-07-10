t = int(input())

def odredi_min(k, lista):
    lista.sort()
    suma = 0
    for i in range(k, 0, -1):
        if len(lista) > 2 and lista[-3] != lista[0]:
            deljenik = lista[-1]
            delilac = lista[-2]
            suma += int(deljenik/delilac)
            del lista[-1]
            del lista[-1]
        else:
            deljenik = lista[0]
            delilac = lista[-i]
            suma += int(deljenik/delilac)
            del lista[-i]
            del lista[0]
    for el in lista:
        suma += el
    return suma


resenje = []
for i in range(t):
    p = input().split(" ")
    prva = [int(el) for el in p]
    l = input().split(" ")
    lista = [int(el) for el in l]
    resenje.append(odredi_min(prva[1], lista))

for i in range(t):
    print(resenje[i])