def provera(unos):
    brojac = 0
    prvi = int(unos[0])
    drugi = int(unos[1])
    ukupno = prvi + drugi
    while 1:
        if prvi > drugi*3 and prvi == int(unos[0]):
            return drugi
        if drugi > prvi*3 and prvi == int(unos[0]):
            return prvi
        if prvi > 3 and drugi > 3 and ukupno >= 4:
            pokusaj = ukupno // 4
            if pokusaj < prvi and pokusaj < drugi:
                brojac += pokusaj
                prvi -= pokusaj
                drugi -= pokusaj
                ukupno -= 4*pokusaj
            elif pokusaj == prvi or pokusaj == drugi:
                return pokusaj
            elif pokusaj > prvi:
                brojac += prvi
                drugi -= prvi
                prvi = 0
                ukupno -= 4*pokusaj
            elif pokusaj > drugi:
                brojac += drugi
                prvi -= drugi
                drugi = 0
                ukupno -= 4*pokusaj
        elif prvi >= 1 and drugi >= 1 and ukupno >= 4:
            brojac += 1
            prvi -= 1
            drugi -= 1
            ukupno -= 4
        else:
            break
    return brojac


t = int(input())
resenje = []

for i in range(t):
    unos = input().split(" ")
    resenje.append(provera(unos))

for el in resenje:
    print(el)