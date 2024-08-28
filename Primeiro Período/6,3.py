V = eval(input())
x = int(input())
i = 0
j = len(V) - 1
def BuscaBinaria(V, x):
    global i
    global j
    if i > j:
        return -1
    m = (i+j)//2
    if V[m] < x:
        i = m + 1
        return BuscaBinaria(V, x)
    elif V[m] > x:
        j = m - 1
        return BuscaBinaria(V, x)
    else:
        return m
print(BuscaBinaria(V, x))