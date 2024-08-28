l = [0, 1]
x = int(input())
z = 0
k = 0
for i in range(x):
    z = int(l[-1]) + int(l[-2])
    l += [z]
if l [-1] > x:
    while l[-1] > x:
        del l[-1]
for i in range(len(l)):
    k += l[i]
print(l)
print(k)