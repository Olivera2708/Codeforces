def sredi(lista):
    jedan = lista[0]
    dva = lista[1]
    if jedan+dva != lista[2]:
        tri = lista[2]
    else:
        tri = lista[3]
    return [jedan, dva, tri]

n = int(input())
gotovo = []

for i in range(n):
    unos = input().split(" ")
    unos_lista = [int(c) for c in unos]
    sredjeno = sredi(unos_lista)
    gotovo.append(sredjeno)

for i in range(n):
    print(f"{gotovo[i][0]} {gotovo[i][1]} {gotovo[i][2]}")
