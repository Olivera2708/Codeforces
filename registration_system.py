n = int(input())

names = []

for i in range(n):
    name = input()
    if i == 0:
        names.append(name)
        print("OK")
    else:
        nasao = True
        for n in names[::-1]:
            nasao = True
            if len(name) <= len(n):
                for j in range(len(name)):
                    if name[j] != n[j]:
                        nasao = False
                        break
                if nasao:
                    if len(name) == len(n):
                        names.append(name+"1")
                        print(name+"1")
                        break
                    elif not n[len(name)].isalpha():
                        num = 0
                        for j in range(len(name), len(n)):
                            num *= 10
                            num += int(n[j])
                        num += 1
                        names.append(name+str(num))
                        print(name+str(num))
                        break
                    else:
                        nasao = False
            else:
                nasao = False

        if not nasao:
            names.append(name)
            print("OK")
    


