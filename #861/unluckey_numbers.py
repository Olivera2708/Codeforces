def print_luckey(number1, number2):
    mini = 10
    maxi = -1

    el = 0
    for i in range(len(number1)):
        if number1[i] != number2[i]:
            el = i
            break
        else:
            if int(number1[i]) < mini:
                mini = int(number1[i])
            if int(number1[i]) > maxi:
                maxi = int(number1[i])

    new_num1 = int(number1[el:])
    new_num2 = int(number2[el:])

    best = -1
    best_n = 10

    for num in range(new_num1, new_num2+1):
        mini1 = mini
        maxi1 = maxi

        is_ok = False
        if mini == maxi:
            is_ok = True
            for nu in str(num):
                if int(nu) != mini:
                    is_ok = False
                    break
        
        if not is_ok:
            for nu in str(num):
                if int(nu) < mini1:
                    mini1 = int(nu)
                if int(nu) > maxi1:
                    maxi1 = int(nu)

            if maxi1 - mini1 < best_n:
                best_n = maxi1 - mini1
                best = number1[:el] + str(num)
        else:
            print(number1[:el] + str(num))
            return

    print(best)


amount = int(input())

for i in range(amount):
    numbers = input().split(" ")
    # if int(numbers[0]) < 10:
    #     print(numbers[0])
    #     break
    print_luckey(numbers[0], numbers[1])