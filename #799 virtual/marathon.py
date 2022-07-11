def odredi(unos):
    br = 0
    for i in unos[1:]:
        if int(unos[0]) < int(i):
            br += 1
    return br

test = int(input())

for i in range(test):
    unos = input().split(" ")
    print(odredi(unos))