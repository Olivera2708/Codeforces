def ucitaj(n):
    matrica = []
    for _ in range(n):
        a = [i for i in input()]
        matrica.append(a)
    return matrica
        
def slova(n):
    minus = 1
    ukupno = 0
    while True:
        if (n - minus > 0):
            ukupno += n - minus
            minus += 2
        else:
            return ukupno
    
def brojanje(matrica, n):
    counter = 0
    sloj = 1
    i = 0
    j = 0
    for b in range(slova(n)):
        lista = [matrica[i][j], matrica[j][n-1-i], matrica[n-i-1][n-j-1], matrica[n-j-1][i]]
        najvece = max(lista)
        for t in range(4):
            counter += ord(najvece) - ord(lista[t])

        if (j < n-sloj-1):
            j += 1
        else:
            j = sloj
            i = sloj
            sloj += 1

    return counter
        

p = int(input())

for _ in range(p):
    n = int(input())
    matrica = ucitaj(n)
    print(brojanje(matrica, n))