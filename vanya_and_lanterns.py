length = int(input().split(" ")[1])
lamps = input().split(" ")
lamps = [int(l) for l in lamps]

lamps.sort()

first = lamps[0]
last = length - lamps[-1]

d = max(first, last)

for i in range(len(lamps)-1):
    if (lamps[i+1]-lamps[i])/2 > d:
        d = (lamps[i+1]-lamps[i])/2

print(d)