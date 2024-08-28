A = eval(input())
B = eval(input())
S = A
k = True
if len(A) != len(B):
    print("Erro!")
    k = False
else:
    if len(A[0]) != len(B[0]):
        print("Erro!")
        k = False
    else:
        for p in range(len(A)):
            for i in range(len(A[p])):
                S[p][i] = A[p][i] + B[p][i]
if k == True: print(S)