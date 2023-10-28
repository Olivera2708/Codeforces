def odredi(x, y, duzine):
    if (provera_slova(x, y)):
        return -1
    counter = 0
    while (counter < duzine[1]):
        if y in x:
            return counter
        
        x += x
        counter += 1
    return -1

def provera_slova(x, y):
    for slovo in y:
        if slovo not in x:
            return True
    return False

n = int(input())

for i in range(n):
    duzine = [int(i) for i in input().split(" ")]
    x = input()
    y = input()

    print(odredi(x, y, duzine))