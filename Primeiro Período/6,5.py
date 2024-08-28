divisores = set()
l = eval(input())
i = 1
j = 0

def procura(x):
    global i, divisores
    lim = x**(1/2)
    if i > lim:
        i = 1
        return divisores
    if x % i == 0:
        div_atual = x // i
        divisores.add(div_atual)
        divisores.add(x // div_atual)
        i += 1
        return procura(x)
    else:
        i += 1
        return procura(x)

def comparador():
    global j, Intersect
    if j == 0:
        C1 = procura(l[j]).copy()
        divisores.clear()
        C2 = procura(l[j + 1]).copy()
        divisores.clear()
        Intersect = C1 & C2
        j += 1
        return comparador()
    elif j == len(l) - 1 and j != 0:
        return Intersect
    else:
        C2 = procura(l[j + 1]).copy()
        divisores.clear()
        Intersect = Intersect & C2
        j += 1
        return comparador()
    
print(comparador())