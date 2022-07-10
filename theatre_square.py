from math import ceil
s = input()
n, m, a = s.split(" ")
konacno = ceil(int(n)/int(a))*ceil(int(m)/int(a))
print(konacno)