class Vetor(list):
    def __init__(self, l):
        self.vetor = l
        self.usados = []
    def mdc(self):
        for i in range(len(self.vetor)):
            if self.vetor[i] < 0 or int(self.vetor[i]) != self.vetor[i]:
                del self.vetor[i]
            else:
                if self.vetor[i] in self.usados:
                    pass
                else:
                    self.usados.append(self.vetor[i])
        MDC = set()
        for i in range(len(self.vetor) - 1):
            MDC.add(max(divisores(self.vetor[i]).intersection(divisores(self.vetor[i + 1]))))
        return tuple(MDC)
    
def divisores(n):
    k = set()
    for i in range(int(n**1/2)):
        if n % (i+1) == 0:
            k.add(i + 1)
            k.add(n // (i + 1))
        i += 1
    return k

print(Vetor(eval(input())).mdc())