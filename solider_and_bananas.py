unos = input()
unos = unos.split(" ")
k = int(unos[0])
n = int(unos[1])
w = int(unos[2])

cena = 0
br = 1

while br <= w:
    cena += br * k
    br += 1

if cena > n:
    print(cena - n)
else:
    print(0)