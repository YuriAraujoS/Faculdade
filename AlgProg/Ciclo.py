class Ciclo:
    def __init__(self, ponto, raio):
        self.raio = raio
        self.coordenadas = ponto
        self.x = ponto[0]
        self.y = ponto[1]

def ponto_in_ciclo(ciclo, ponto):
    if ((ciclo.x - ponto[0]) ** 2 + (ciclo.y - ponto[1]) ** 2) <= (ciclo.raio) ** 2:
        return True
    else:
        return False

def retangulo_in_ciclo(ciclo, v1, v2, v3, v4):
    if ponto_in_ciclo(ciclo, v1) == True and ponto_in_ciclo(ciclo, v2) == True and ponto_in_ciclo(ciclo, v3) == True and ponto_in_ciclo(ciclo, v4) == True:
        return True
    else:
        return False

print(ponto_in_ciclo(Ciclo(eval(input()), int(input())), eval(input())))