A = eval(input())
det = 0
for i in range(len(A)):
    B = A.copy()
    del B[i]
    for k in range(len(B)):
        if len(B[k]) > len(A) - 1:
            del B[k][0]
    for m in range(len(B) - 1):
        B.append(B[m])
    #B está feita.
    soma = 0
    subtração = 0
    for p in range(len(A) - 1):
        m_menos = 1
        m_mais = 1
        for j in range(len(B) - 1):
            m_mais *= B[j][j + p - 1]
            m_menos *= B[-j][j + p - 1]
        soma += m_mais
        subtração += m_menos
    cofator = (soma - subtração) * (-1)**(i + 0)
    det += cofator
    print(B)
print(det)