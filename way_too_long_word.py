n = int(input())
skraceno = []
for i in range(n):
    uneseno = input()
    if len(uneseno) > 10:
        skraceno.append(f"{uneseno[0]}{len(uneseno)-2}{uneseno[-1]}")
    else:
        skraceno.append(uneseno)
for i in range(n):
    print(skraceno[i])
