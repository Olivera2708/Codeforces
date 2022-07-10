def svi_isti(lista):
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            return False
    return True

def isprobaj(broj, lista):
    sortirana = [el for el in lista]
    sortirana.sort()
    sortirana1 = set(sortirana)
    if len(sortirana1) == 1:
        m = list(sortirana1)[0]
    else:
        m = list(sortirana1)[1]
    if not svi_isti(lista):
        return 0
    for i in range(m, 1, -1):
        for j in range(broj-1):
            if (lista[j] % i == 0 and lista[j+1] % i != 0) or (lista[j] % i != 0 and lista[j+1] % i == 0):
                if j == broj-2:
                    return i
                continue
            else:
                break
    return 0


n = int(input())
konacno = []
for i in range(n):
    br_el = int(input())
    unos = input().split(" ")
    lista = [int(el) for el in unos]
    resenje = isprobaj(br_el, lista)
    konacno.append(resenje)

for i in range(n):
    print(konacno[i])