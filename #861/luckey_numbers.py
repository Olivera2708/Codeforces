def find_luckey(n):
    mini = 10
    maxi = -1
    for e in str(n):
        if int(e) > maxi:
            maxi = int(e)
        if int(e) < mini:
            mini = int(e)
    return maxi-mini
        

def print_luckey(start, end):
    best = -1
    luckey = -1
    for i in range(start, end + 1):
        l = find_luckey(i)
        if l > luckey:
            luckey = l
            best = i
        if luckey == 9:
            break
    
    print(best)



amount = int(input())

for i in range(amount):
    numbers = input().split(" ")
    numbers = [int(n) for n in numbers]
    print_luckey(numbers[0], numbers[1])