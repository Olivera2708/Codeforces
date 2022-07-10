n = int(input())
x = 0
y = 0
z = 0

for i in range(n):
    l = input().split(" ")
    li = [int(el) for el in l]
    x += li[0]
    y += li[1]
    z += li[2]

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
