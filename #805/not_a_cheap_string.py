def izracunaj(w, p):
    dict = {}
    ukupno = 0
    rez = {}
    for index, slovo in enumerate(w):
        if not (slovo in dict.keys()):
            ukupno += ord(slovo) - 96
            dict[slovo] = [ord(slovo) - 96, 1]
        else:
            ukupno += dict[slovo][0]
            dict[slovo][1] += 1

    if ukupno <= p:
        return w

    sort_dict = sorted(dict.items(), key = lambda x: x[1][0])

    uk = 0
    prekoraceno = False
    for s in sort_dict:
        if prekoraceno:
            break
        for i in range(s[1][1]):
            uk += s[1][0]
            if (uk > p):
                prekoraceno = True
                break
            else:
                if s[0] in rez.keys():
                    rez[s[0]] += 1
                else:
                    rez[s[0]] = 1
    
    res = ""
    for slovo in w:
        if slovo in rez.keys() and rez[slovo] != 0:
            res += slovo
            rez[slovo] -= 1

    return res

br_test = int(input())

for i in range(br_test):
    w = input()
    p = int(input())
    print(izracunaj(w, p))