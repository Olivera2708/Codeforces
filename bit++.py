n = int(input())
broj = 0
for i in range(n):
    string = input()
    if "+" in string:
        broj += 1
    else:
        broj -= 1
print(broj)