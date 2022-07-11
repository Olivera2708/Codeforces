def pronadji(tabla):
    resenje = []
    rez = []
    for i in range(0, 8):
        broj = 0
        cuvar = []
        for j in range(0, 8):
            if (tabla[i][j] == "#"):
                cuvar.append([i, j])
                broj += 1
        resenje.append(broj)
        if broj == 1:
            rez.append(cuvar[0])
        else:
            rez.append([])
    for i in range(1, 7):
        if resenje[i] == 1 and resenje[i-1] == 2 and resenje[i+1] == 2:
            return f"{rez[i][0] + 1} {rez[i][1] + 1}"

        


test = int(input())

for i in range(test):
    tabla = []
    input()
    for i in range(8):
        tabla.append([x for x in input()])
    print(pronadji(tabla))