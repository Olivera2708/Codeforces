def provera(segment):
    global recnik, prvi, drugi
    if (segment[0] == "+"):
        if ((int(segment[1]), int(segment[2])) not in recnik):
            recnik[(int(segment[1]), int(segment[2]))] = 1
        else:
            recnik[(int(segment[1]), int(segment[2]))] += 1
    else:
        if (recnik[(int(segment[1]), int(segment[2]))] == 1):
            del recnik[(int(segment[1]), int(segment[2]))]

            if (len(recnik) == 0):
                prvi = 0
                drugi = 1000000000
            else:
                if (int(segment[1]) == prvi):
                    recnikPoPrvom = dict(sorted(recnik.items(), key=lambda x: x[0]))
                    prvi = list(recnikPoPrvom.keys())[-1][0]

                if (int(segment[2]) == drugi):
                    recnikPoDrugom = dict(sorted(recnik.items(), key=lambda x: x[0][1]))
                    drugi = list(recnikPoDrugom.keys())[0][1]
        else:
            recnik[(int(segment[1]), int(segment[2]))] -= 1

    if (len(recnik) > 1 and drugi < prvi):
        return "YES"
    else:
        return "NO"


n = int(input())
recnik = {}
prvi = 0
drugi = 1000000000

for k in range(n):
    segment = [i for i in input().split(" ")]

    if (prvi < int(segment[1])):
        prvi = int(segment[1])
    if drugi > int(segment[2]):
        drugi = int(segment[2])

    print(provera(segment))