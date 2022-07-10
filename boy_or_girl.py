ime = input()
num = 0

lista = [c for c in ime]
setted = set(lista)
num = len(setted)


if num % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")