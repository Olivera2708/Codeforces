import math

test_broj = int(input())

unos = []

for i in range(test_broj):
    unos.append(input())

for rec in unos:
    br_slova = 0
    dan = 0;
    slova = []
    for slovo in rec:
        if br_slova == 3 and slovo not in slova:
            br_slova = 0
            dan += 1
            slova.clear()

        if slovo not in slova:
            slova.append(slovo)
            br_slova += 1
    
    if (br_slova != 0):
        print(dan + 1)
    else:
        print(dan)
