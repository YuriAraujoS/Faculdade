x = input()
def numero_caracteres(x):
    return len(x)
def inversão(x):
    return int(x[::-1])
print([numero_caracteres(x), inversão(x)])