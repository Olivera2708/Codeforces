def provera(string):
    if string[0] == string[4] and string[1] == string[3]:
        return True
    return False

def dodaj_vreme(vreme, mint):
    podeli = vreme.split(":")
    minut = int(podeli[1]) + int(mint)
    sati = int(podeli[0])
    minuti = int(podeli[1])
    if minut >= 60:
        dodaj = minut//60
        ostatak = minut - dodaj*60
        sati = int(podeli[0]) + dodaj
        minuti = ostatak
    else:
        minuti = minut
    if sati > 23:
        sati -= 24
    string_sati = ""
    string_minuti = ""
    if sati == 0:
        string_sati = "00"
    elif sati < 10:
        string_sati = f"0{sati}"
    else:
        string_sati = f"{sati}"
    if minuti == 0:
        string_minuti = "00"
    elif minuti < 10:
        string_minuti = f"0{minuti}"
    else:
        string_minuti = f"{minuti}"
    return f"{string_sati}:{string_minuti}"
    

def palindromi(vreme, minuti):
    br = 0
    pocetno_vreme = vreme
    menjam = vreme
    if provera(vreme):
        br += 1
    menjam = dodaj_vreme(menjam, minuti)
    while pocetno_vreme != menjam:
        if provera(menjam):
            br += 1
        menjam = dodaj_vreme(menjam, minuti)
    return br

test = int(input())

for i in range(test):
    unos = input().split(" ")
    print(palindromi(unos[0], unos[1]))