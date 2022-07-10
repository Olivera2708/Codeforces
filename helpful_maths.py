unos = input()
broj = [0, 0, 0]

for c in unos:
    if c == "1":
        broj[0] += 1
    elif c == "2":
        broj[1] += 1
    elif c == "3":
        broj[2] += 1

novi = ""
for i in range(broj[0]):
    novi += "1+"
for i in range(broj[1]):
    novi += "2+"
for i in range(broj[2]):
    novi += "3+"

print(novi[:-1])