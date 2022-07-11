def jeste(niz, poslednji, broj, el):
    if broj == 1:
        return True
    if len(niz) < broj-1:
        return False
    if poslednji < niz[0] * el:
        return jeste(niz[1:], niz[0] * el, broj-1, el*2)
    else:
        return False

def brojac(niz, broj):
    brojac = 0
    for i in range(len(niz)-broj+1):
        if jeste(niz[i+1:], niz[i], broj, 2):
            brojac += 1
    return brojac

test = int(input())

for i in range(test):
    broj = int(input().split(" ")[1]) + 1
    niz = [int(x) for x in input().split(" ")]
    print(brojac(niz, broj))