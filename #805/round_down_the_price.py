def res(br):
    moj = 1
    while (br >= moj):
        moj *= 10

    if (moj > 1):
        print(br - moj//10)
    else:
        print(br - moj) 

test_broj = int(input())

for i in range(test_broj):
    res(int(input()))
