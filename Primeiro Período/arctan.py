val = float(input())
tam = int(input())
arco = 0
i = 1

def arctan(x, n):
    global arco, i
    for k in range(n):
        if (i - 1) % 4 == 0:
            arco += (x**i) / i
            k += 1
        else:
            arco -= (x**i) / i
            k += 1
        i += 2
    return arco

print(arctan(val, tam))