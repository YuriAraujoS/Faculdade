A = eval(input())
n = A[0]
a = A[1]
b = A[2]
c = A[3]
S = 0
for i in range(n):
    S += ((-1)**(c + (i + 1)))*((1 +a * (i + 1))/(3*(b ** (i + 1))))
print(round(S, 3))