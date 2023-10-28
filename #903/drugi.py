n = int(input())

def pokusaj(duzine):
    for _ in range(3):
        maxi = max(duzine)
        mini = min(duzine)
        if (maxi == mini):
            return "YES"

        nov = maxi - mini

        duzine.remove(maxi)
        if (nov >= mini):
            duzine.append(nov)
            duzine.append(mini)
        else:
            nov = maxi//2
            novi = maxi-nov
            duzine.append(nov)
            duzine.append(novi)

    maxi = max(duzine)
    mini = min(duzine)
    if (maxi == mini):
        return "YES"
    return "NO"

for _ in range(n):
    duzine = [int(i) for i in input().split(" ")]
    print(pokusaj(duzine))