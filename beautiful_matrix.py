matrix = []
red = -1
kolona = -1
for i in range(5):
    linija = input().split(" ")
    matrix.append(linija)
    if "1" in linija:
        red = i
        kolona = linija.index("1")
broj_poteza = abs(2-red) + abs(2-kolona)
print(broj_poteza)