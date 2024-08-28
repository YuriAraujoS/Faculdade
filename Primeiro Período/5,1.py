A = eval(input())
B = eval(input())
if len(A[0]) != len(B):
    print("Erro!")
else:
    P = []
    for i in range(len(A)):
        T = []
        for k in range(len(B[0])):
            elemento = 0
            for j in range(len(B)):
                elemento += A[i][j] * B[j][k]
            T.append(elemento)
        P.append(T)
    print(P)