string = input().lower()
vowels = ["a", "o", "y", "e", "u", "i"]
new = ""

for c in string:
    if c in vowels:
        continue
    new += f".{c}"

print(new)