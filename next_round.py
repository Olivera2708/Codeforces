prva = input().split(" ")
druga = input().split(" ")
br = 0
while 1:
    if int(prva[0]) > br and int(druga[br]) >= int(druga[int(prva[1])-1]) and int(druga[br]) > 0:
        br += 1
    else:
        break
print(br)