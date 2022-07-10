def vrati(u, lista):
    try:
        if u[lista[0]][0] < u[lista[1]][-1]:
            return "YES"
        else:
            return "NO"
    except:
        return "NO"

br_test = int(input())
rez = []
for i in range(br_test):
    input()
    linija1 = input().split(" ")
    n = int(linija1[0])
    k = int(linija1[1])
    u = input().split(" ")
    dict = {}
    br = 1
    for el in u:
        if el in dict.keys():
            dict[el].append(br)
        else:
            dict[el] = [br]
        br+= 1

    for i in range(k):
        print(vrati(dict, input().split(" ")))
    