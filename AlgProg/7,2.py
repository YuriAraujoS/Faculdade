M = eval(input())
i = 0
j = 0
Vi = 0
Vj = 0
caminho = []

def caminho_diagonal(L):
    global i, j, Vi, Vj, caminho
    Testando = False
    if L[i + Vi][j + 1] == 1 and L[i + 1][j + Vj] == 1:
        return False
    if L[0][0] == 1:
        return False
    if j + Vi == i + Vi and j + Vj == len(L) - 2:
        return caminho
    if L[i + 1][j + Vj] == 0:
        if L[i + 1][j + Vj] == L[i + Vi][j + 1] and L[i + 1][j + Vj] == 0:
            save = i
            if i != len(L) - 2:
                i += 1
            else :
                Vi = 1
            Testando = True
            #if caminho_diagonal(L) == False:
            #    i = save
            #    j += 1
            #    caminho.append((i + Vi, j + Vj))
            #    return caminho_diagonal(L)
        else:
            if i != len(L) - 2:
                i += 1
            else:
                Vi = 1
            Testando = False
            caminho.append((i + Vi, j + Vj))
            return caminho_diagonal(L)
    if L[i + Vi][j + 1] == 0:
        if j != len(L[0]) - 2:
            j += 1
        else:
            Vj = 1
        j += 1
        caminho.append((i + Vi, j + Vj))
        return caminho_diagonal(L)

print(caminho_diagonal(M))