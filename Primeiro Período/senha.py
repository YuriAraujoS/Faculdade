class Senha:
    def __init__(self, senha):
        self.senha = senha
        self.jogadas = []
        self.tentativas = 0
        self.possibilidades = "rboypgw"
        self.mostrar = False
        self.representação = [["*", " ", "||"], ["*", " ", "||"], ["*", " ", "||"], ["*", " ", "||"]]

    def chutar(self, tentativa):
        for i in range(len(tentativa)):
            if tentativa[i] not in self.possibilidades:
                raise ValueError
        if len(tentativa) != 4:
            raise ValueError
        elif tentativa in self.jogadas:
            raise IndexError
        else:
            if tentativa == self.senha:
                self.vitória = True
                self.mostrar = True
            else:
                self.jogadas.append(tentativa)
                self.jogadas += 1
                print(self)
                if self.jogadas == 10:
                    self.mostrar = True
                    print("Você Errou")

    def avaliar(self):

    def __repr__(self):
        