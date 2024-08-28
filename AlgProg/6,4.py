V = eval(input())
i = 0
j = len(V) - 1
k = 0
Ordenado = []

def BuscaBinaria(V, x):
    global i, j, Ordenado
    if i > j:
        if x > V[m]:
            Ordenado.insert[m + 1, x]
            print(Ordenado)
            Ordenador()
        else:
            Ordenado.insert[m - 1, x]
            print(Ordenado)
            Ordenador()
    m = (i+j)//2
    if V[m] < x:
        i = m + 1
        return BuscaBinaria(V, x)
    elif V[m] > x:
        j = m - 1
        return BuscaBinaria(V, x)

def Ordenador():
    global k, x
    if k == len(V):
        return Ordenado
    else:
        x = V[k]
        k += 1
        return BuscaBinaria(V, x)

print(Ordenador())