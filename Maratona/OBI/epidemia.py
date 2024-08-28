#N¹(R^n - 1)/R - 1 > P

N = int(input())
R = int(input())
P = int(input())

max = False
n = 1

if n != 1:
    while max == False:
        K = N * (R**n - 1) / (R - 1)
        print(K)
        if K >= P:
            max = True
            n -= 1
        else:
            n += 1

else:
    while max == False:
        K = N * n
        if K >= P:
            max = True
            n -= 1
        else:
            n += 1
