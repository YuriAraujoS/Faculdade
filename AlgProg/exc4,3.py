M = eval(input())
resp = False
d1 = 0
d2 = 0
for i in range(len(M)):
    x = sum(M[i])
    y = 0
    for j in range(len(M)):
        if j == i:
            d1 += M[i][j]
        if j + i == len(M) - 1:
            d2 += M[i][j]
        y += M[j][i]
    if i == 0:
        z = y
    if y == z:
        z = y
    else:
        break
    if x == sum(M[i]):
        x = sum(M[i])
    else:
        break
if d1 == x and d2 == x and y == x:
    resp = True
print(resp)