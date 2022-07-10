n = int(input())
list = []
sum = 0
for i in range(n):
    list.append(input())
for el in list:
    if el.count("1") > 1:
        sum += 1
print(sum)
