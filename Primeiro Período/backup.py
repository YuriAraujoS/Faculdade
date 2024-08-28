In = eval(input())
K = In[1]
M = In[0]
i = 0
j = 0
caminho = [(0,0)]

def caminho_diagonal(L):
    global i
    if L[0][0] == 1:
        return False
    elif L[len(L) - 1][len(L[0]) - 1] == 1:
        return False
    elif caminho[len(caminho) - 1] == (len(L) - 1, len(L[0]) - 1):
        return caminho
    if caminho[i][1] != len(L[0]) - 1: 
        if L[caminho[i][0]][caminho[i][1] + 1] == 1 and L[caminho[i][0] + 1][caminho[i][1]] == 1:
            return False  
        if L[caminho[i][0]][caminho[i][1] + 1] == 0:
            caminho.append((caminho[i][0], caminho[i][1] + 1))
            i += 1
            return caminho_diagonal(L)
    if caminho[[i][0]] != len(L) - 1:
        if L[caminho[i][0] + 1][caminho[i][1]] == 1:
            return False
        if L[caminho[i][0] + 1][caminho[i][1]] == 0:
            caminho.append((caminho[i][0] + 1, caminho[i][1]))
            i += 1
            return caminho_diagonal(L)

def verifica_caminho_diagonal(C):
    global j
    if C != []:
        if C[len(C) - 1][0] == len(M) - 1 and C[len(C) - 1][1] == len(M[0]) and j == len(C - 1):
            return True
        if M[C[j][0]][C[j][1]] == 1 or C[j][0] < C[j - 1][0] or C[j][1] < C[j - 1][0]:
            return False
        else:
            j += 1
            return True
    else:
        return False
    
print(caminho_diagonal(M), verifica_caminho_diagonal(K))