broj = int(input())
izgled = input()

brojac = 0

for i in range(broj-1):
    if izgled[i] == izgled[i+1]:
        brojac += 1

print(brojac)