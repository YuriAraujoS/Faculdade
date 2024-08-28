In = eval(input())
i = 0
j = 0


caminho = [(0,0)]
Test = False
save = 0

def caminho_diagonal(L):
    global i, save, Test
    if L[0][0] == 1:
        return False
    elif L[len(L) - 1][len(L[0]) - 1] == 1:
        return False
    elif caminho[len(caminho) - 1] == (len(L) - 1, len(L[0]) - 1):
        return caminho
    if caminho[i][1] != len(L[0]) - 1:
        if caminho[i][0] != len(L) - 1:
            if L[caminho[i][0]][caminho[i][1] + 1] == 1 and L[caminho[i][0] + 1][caminho[i][1]] == 1:
                return False
        else:
            if L[caminho[i][0]][caminho[i][1] + 1] == 1:
                return False
        if caminho[i][0] != len(L) - 1:
            if L[caminho[i][0]][caminho[i][1] + 1] == 0 and L[caminho[i][0] + 1][caminho[i][1]] == 0 and Test == False:
                save = i
                Test = True
                caminho.append((caminho[i][0], caminho[i][1] + 1))
                i += 1
                if caminho_diagonal(L) == False:
                    for pos in range(i - save):
                        del caminho[-1]
                        pos += 1
                    Test = False
                    i = save
                    L[caminho[i][0]][caminho[i][1] + 1] = 1
                    return caminho_diagonal(L)
                else:
                    return caminho_diagonal(L)
        else:
            caminho.append((caminho[i][0], caminho[i][1] + 1))
            i += 1
            return caminho_diagonal(L)
    if caminho[i][0] != len(L) - 1:
        if caminho[i][1] == len(L[0]) - 1:
            if L[caminho[i][0] + 1][caminho[i][1]] == 1:
                return False
        else: 
            caminho.append((caminho[i][0] + 1, caminho[i][1]))
            i += 1
            return caminho_diagonal(L)

def verifica_caminho_diagonal(C):
    global j
    if C != []:
        if C[len(C) - 1][0] == len(In[0]) - 1 and C[len(C) - 1][1] == len(In[0][0]) and j == len(C - 1):
            return True
        if In[0][C[j][0]][C[j][1]] == 1 or C[j][0] < C[j - 1][0] or C[j][1] < C[j - 1][0]:
            return False
        else:
            j += 1
            return True
    else:
        return False

print((caminho_diagonal(In[0]), verifica_caminho_diagonal(In[1])))