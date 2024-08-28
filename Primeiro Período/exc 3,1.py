x = input()
y = input()
m = 0
u = 0
q = False
for i in range(len(x)):
    k = x[i]
    for p in range(len(y) - u):
        if k == y[p + u]:
            m += 1
            u += p
            break
if m == len(x):
    print(True)
else:
    print(False)