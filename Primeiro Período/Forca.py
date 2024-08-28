class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.tam = len(palavra)
        self.decifrar = []
        for i in range(self.tam):
            self.decifrar.append("_")
        self.jogadas = ""
        self.erros = 0
        self.fim = False
        self.jogar(input())

    def mostrar(self):
        vazia = ""
        for i in range(self.tam):
            vazia += self.decifrar[i]
        return vazia

    def jogar(self, letra):
        if (letra in self.jogadas) or len(letra) != 1:
            print(f"Palpite Inválido: {letra}" )
        else:
            if letra in self.palavra:
                for i in range(self.tam):
                    if self.palavra[i] == letra:
                        self.decifrar[i] = self.palavra[i]
                self.jogadas += letra
                print(self.mostrar())
                if self.fim == False:
                    self.jogar(input())
                if self.mostrar() == self.palavra:
                    self.fim = True
                    print("Você ganhou")
            else:
                self.erros += 1
                self.jogadas += letra
                print(self.mostrar())
                if self.erros == 6:
                    self.fim = True
                    print("Você perdeu")
                if self.fim == False:    
                    self.jogar(input())

    def __repr__(self):
        return self.mostrar()
    
Forca(input())