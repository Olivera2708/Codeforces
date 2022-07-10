unos = input()

tacno = False
trenutni = ""
brojac = 0

for c in unos:
    if c == trenutni:
        brojac += 1
        if brojac == 7:
            tacno = True
            break
    else:
        trenutni = c
        brojac = 1

if tacno:
    print("YES")
else:
    print("NO")