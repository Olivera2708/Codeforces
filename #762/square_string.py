def square(string):
    duzina = int(len(string)/2)
    if len(string) % 2 != 0:
        return "NO"
    else:
        if string[:duzina] == string[duzina:]:
            return "YES"
        else:
            return "NO"

n = int(input())

result = []
for i in range(n):
    string = input()
    result.append(square(string))

for i in result:
    print(i)