input()

numbers = input().split(" ")
numbers = [int(n) for n in numbers]

even = 0
odd = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even += 1
        if odd > 1:
            print(i+1)
            break
    else:
        odd += 1
        if even > 1:
            print(i+1)
            break

    if even > 1 and odd == 1:
        for j in range(3):
            if numbers[j] % 2 != 0:
                print(j+1)
                break
        break
    if even == 1 and odd > 1:
        for j in range(3):
            if numbers[j] % 2 == 0:
                print(j+1)
                break
        break
