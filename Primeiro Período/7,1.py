Vetor : list = eval(input())
tam = len(Vetor)
Resp= []
j = 0

def Ordenador():
    global Resp, Vetor, j
    menor = 0
    if len(Vetor) == 0:
        return Resp
    for i in range(len(Vetor)):
        if Vetor[i] < Vetor [menor]:
            menor = i
    Resp.append(Vetor.pop(menor))
    return Ordenador()

print(Ordenador())