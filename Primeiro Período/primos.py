intervalo = int(input())
i = 1
k = 1
L = []
conjunto = []

def primo(x):
    global i, L
    if i > x ** 1/2:
        i = 1
        if len(L) == 2:
            L = []
            return True
        else:
            L = []
            return False
    if x // i == x / i:
        L.append(i)
        L.append(x // i)
        i += 1
        return primo(x)
    else:
        i += 1
        return primo(x)

def primoscirculares(n):
    global conjunto, k
    for k in range(n + 1):
        if primo(k) == True:
            p = str(k)
            circular = int(p)
            quantidade = 0
            for j in range(len(p)):
                p += p[0]
                p = p[1:]
                circular = int(p)
                if primo(circular) == True:
                    quantidade += 1
                    if quantidade == len(p):
                        conjunto.append(k)
                j += 1
            k += 1
        else:
            k += 1
    return conjunto

print(primoscirculares(intervalo))