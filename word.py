word = input()

big = 0
small = 0

for letter in word:
    if letter.upper() == letter:
        big += 1
    else:
        small += 1

if big > small:
    print(word.upper())
else:
    print(word.lower())