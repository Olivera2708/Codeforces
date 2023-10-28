najbolje = 0
najbolje1 = 0

def unutrasnje(lista, n):
    prvi = lista[0]
    sledeci = lista[prvi+1]

    if (sledeci ==  n - prvi - 2):
        return 
    elif (sledeci == n-1):
        najbolje1 = najbolje
    elif (sledeci > n - prvi - 2):
        del lista[sledeci]
        najbolje1 += 1
        unutrasnje(lista, n-1)

def izracunaj(lista, n):
    br = n
    while True:
        if (len(lista) == 0):
            najbolje = n
            najbolje1 = n
            break
        if (lista[0] > br-1):
            del lista[0]
            br -= 1
        elif (lista[0] == br-1):
            najbolje = n-br
            najbolje1 = n-br
            break
        else:
            najbolje = n-br
            najbolje1 = n-br
            unutrasnje(lista, br)

k = int(input())
for _ in range(k):
    n = int(input())
    lista = [int(i) for i in input().split(" ")]
    izracunaj(lista, n)
    print(najbolje)