def izracunaj(broj):
    sum = 0
    trenutni = 1
    for br in broj:
        if br == 0:
            br = 10
        sum += abs(br - trenutni) + 1
        trenutni = br
    return sum

n = int(input())

for _ in range(n):
    broj = [int(i) for i in input()]
    print(izracunaj(broj))