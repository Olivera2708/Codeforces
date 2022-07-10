def uradi(broj, unos):
    rec = ""
    for i in range(broj-2):
        if i == 0:
            rec += unos[i][0]
        if i == broj-3:
            rec += unos[i][1]
            continue
        if unos[i][1] == unos[i+1][0]:
            rec += unos[i][1]
        else:
            rec += unos[i][1]
            rec += unos[i+1][0]
    if len(rec) != broj:
        rec += "a"
    return rec


n = int(input())
resenja = []

for i in range(n):
    broj = int(input())
    unos = input().split(" ")
    el = uradi(broj, unos)
    resenja.append(el)

for i in range(n):
    print(resenja[i])