A = eval(input())
x = bool(A[0])
y = str(A[1])
z = int(A[2])
caracteres = "abcdefghihjklmnopqrstuvwxyz"
invertida = caracteres[::-1]
def code(y):
    saida = ""
    for i in range(len(y)):
        h = int(caracteres.find(y[i]))
        if h + z > 26:
            saida += invertida[26 - h - z + 1]
        else:
            saida += caracteres[h + z]
    return saida
def decode(y):
    codificada = code("abcdefghihjklmnopqrstuvwxyz")
    saida = ""
    for i in range(len(y)):
        h = int(codificada.find(y[i]))
        saida += caracteres[h]
    return saida
if x == False:
    print(decode(y))
else:
    print(code(y))