linija = input()
linija = linija.split(" ")
a = int(linija[0])
b = int(linija[1])

godina = 0
while a <= b:
    a *= 3
    b *= 2
    godina += 1

print(godina)
