coordinate = int(input())

counter = 0

while True:
    if coordinate <= 5:
        if coordinate > 0:
            counter += 1
        break
    coordinate -= 5
    counter += 1

print(counter)