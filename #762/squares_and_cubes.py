from math import sqrt

def lista(broj):
    lista = []
    for i in range(1, int(sqrt(broj)) + 1):
        lista.append(i**2)
        lista.append(i**3)
    nova = list(dict.fromkeys(lista))
    nova.sort()
    return nova

def izracunaj(broj):
    br = 0
    for el in lista(broj):
        if el <= broj:
            br += 1
        else:
            return br
    return br

n = int(input())
result = []
for i in range(n):
    broj = int(input())
    result.append(izracunaj(broj))

for i in result:
    print(i)