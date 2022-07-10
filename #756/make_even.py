def ima_paran(broj):
    while broj % 10 != 0:
        if broj % 2 == 0:
            return True
        broj = broj // 10
    return False

def paran(lista):
    return lista[-1] % 2 == 0

def nadji_paran(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            return i

def proveri(broj):
    brojac = 0
    lista = [int(el) for el in str(broj)]
    if not ima_paran(broj):
        return -1
    elif paran(lista):
        return 0
    else:
        while not paran(lista):
            if nadji_paran(lista) == 0:
                lista.reverse()
                brojac += 1
            else:
                pomocna = [lista[i] for i in range(nadji_paran(lista)+1)]
                pomocna.reverse()
                pomocna = pomocna + lista[nadji_paran(lista)+1:]
                lista = pomocna
                brojac += 1
        return brojac

t = int(input())
brojevi = []
resenja = []
for i in range(t):
    brojevi.append(int(input()))
    resenja.append(proveri(brojevi[i]))

for el in resenja:
    print(el)