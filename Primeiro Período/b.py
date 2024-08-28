#lista externa
divisores_referencia = []

def funcao(x):
    global divisores_referencia

    #lista interna
    divisores = []

    #looping para achar os divisores
    for i in range(1, int(x/2)):
        if x%i == 0:
            divisores.append(i)
    divisores.append(x)

    #se quiser visualizar tira o comentário desse print
    #print(divisores_referencia, divisores)

    #se for o primeiro valor
    if len(divisores_referencia) == 0:
        divisores_referencia = divisores[:]

    # apartir do 2 valor
    #comparando
    else:
        #ordenando as duas listas para saber qual é menor
        t = [divisores, divisores_referencia]
        t.sort()
        #lista para comparação
        comp = []
        #looping de comparação
        for k in t[0]:
            if k in t[1]:
                comp.append(k)
        #jogando a lista de comparação pra fora da função
        divisores_referencia = comp[:]

for i in [12, 48, 60]:
    funcao(i)

print(divisores_referencia)