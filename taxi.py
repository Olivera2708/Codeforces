import math

input()
groups = input().split(" ")
groups = [int(g) for g in groups]

groups.sort()

begin = 0
end = len(groups) - 1
counter = 0

while begin <= end:
    if (groups[end] == 3 and groups[begin] == 1) or (groups[end] == 2 and groups[begin] == 2):
        counter += 1
        end -= 1
        begin += 1
    elif groups[end] == 2 and groups[begin] == 1:
        if (groups[begin+1] == 1):
            begin += 2
            end -= 1
            counter += 1
        else:
            counter += 1
            end -= 1
            begin += 1
    elif groups[end] == 1 and groups[begin] == 1:
        num = end-begin+1
        counter += math.ceil(num/4)
        break
    else:
        counter += 1
        end -= 1

print(counter)