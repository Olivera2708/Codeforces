def izracunaj(unos):
    duzina = len(unos[0])
    rez = ""
    br = 0
    for i in range(duzina):
        try:
            if int(unos[0][-1-i]) <= int(unos[1][-1-br]):
                broj = int(unos[1][-1-br]) - int(unos[0][-1-i])
                br += 1
                rez = str(broj) + rez
            else:
                if int(unos[1][-2-br]) != 1:
                    return -1
                broj = int(unos[1][-1-br]) + 10 - int(unos[0][-1-i])
                br += 2
                rez = str(broj) + rez 
        except IndexError:
            return -1
    if br <= len(unos[1]) and len(unos[1]) != len(unos[0]):
        rez = unos[1][0:len(unos[1])-br] + rez
    for i in rez:
        if i == "0" and len(rez) != 1:
            rez = rez[1:]
        else:
            break
    return rez


n = int(input())
rezultat = []
for i in range(n):
    unos = input().split(" ")
    rezultat.append(izracunaj(unos))

for i in rezultat:
    print(i)