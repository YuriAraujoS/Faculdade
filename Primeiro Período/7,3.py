divisores = set()
i = 1
Resp = []

def procura(x):
    global i, divisores
    x = int(float(x))
    lim = x ** (1/2)
    if i > lim:
        i = 1
        return divisores
    if int(x) % i == 0:
        div_atual = x // i
        divisores.add(div_atual)
        divisores.add(x // div_atual)
        i += 1
        return procura(x)
    else:
        i += 1
        return procura(x)

def Ordenador(K):
    global Resp, j
    menor = 0
    if len(K) == 0:
        return Resp
    for i in range(len(K)):
        if K[i] < K[menor]:
            menor = i
    Resp.append(K.pop(menor))
    return Ordenador(K)

class Vetor(list):
    def mdc(self):
        mdc = []
        for i in range(len(self)):
            if self[i] is float and self[i] / int(self[i]) != 1:
                i += 1
            if i == 0:
                intersect = procura(self[i]).copy()
                i += 1
            else:
                divisores.clear()
                intersect = procura(self[i]).copy() & intersect
                i += 1
        if intersect == {}:
            return mdc
        else:
            save = ()
            while intersect != {}:
                    if intersect == set():
                        return Ordenador(mdc)
                    k = tuple(intersect.pop())
                    y = ()
                    y = k + save
                    save = y
            return y

v = Vetor(eval(input()))
print(v.mdc())