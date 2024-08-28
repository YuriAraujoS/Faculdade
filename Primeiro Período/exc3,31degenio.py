x = input()
y = input()
q = False
pos = 0
for i in range(len(y)):
    if(x[pos] == y[i]): pos += 1
if pos == len(x):
    print(True)
else:
    print(False)