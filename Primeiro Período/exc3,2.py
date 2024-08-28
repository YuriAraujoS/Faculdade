frase = input()
caracteres = len(frase)
numeros = 0
simbolos = 0
letras = 0
espaços = 0
for i in range(len(frase)):
        if(frase[i] >= "0" and frase[i] <= "9"):
            numeros += 1
for i in range(len(frase)):
    if(frase[i].isalpha() == True):
        letras += 1
for i in range(len(frase)):
    if(frase[i] == " "):
        espaços += 1
palavras = espaços + 1
simbolos = caracteres - numeros - letras
print(caracteres, letras, numeros, simbolos, palavras)