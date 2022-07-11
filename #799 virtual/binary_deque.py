import collections

def izracunaj(niz):
    br = 0
    for i in niz:
        br += int(i)
    return br

def racun(niz1, niz2, suma, br):
    global mini
    if not niz1:
        return 0
    if sum(niz1) < suma:
        return 0
    if sum(niz1) == suma:
        if br < mini:
            mini = br
        return 0
    
    niz1.pop()
    racun(niz1, niz1, suma, br+1)
    niz2.popleft()
    racun(niz2, niz2, suma, br+1)

test = int(input())

for i in range(test):
    suma = int(input().split(" ")[1])
    niz = input().split(" ")
    mini = float('inf')
    niz1 = [int(x) for x in niz]
    racun(collections.deque(niz1), collections.deque(niz1), suma, 0)
    if mini != float('inf'):
        print(mini)
    else:
        print(-1)
