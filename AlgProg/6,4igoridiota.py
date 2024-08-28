V = eval(input())
l = [V[0]]
i = 0
def BuscaBinaria(V, x):
    global i
    global j
    m = (i+j)//2
    if i > j:
        if item >= l[m]:
            return m + 1
        else:
            return m - 1
    else:
        if V[m] < x:
            i = m + 1
            return BuscaBinaria(V, x)
        elif V[m] > x:
            j = m - 1
            return BuscaBinaria(V, x)
        else:
            return m

for item in V[1:]:
    j = len(l) - 1
    pos = BuscaBinaria(l, item)
    l.insert(pos, item)
print(l)
