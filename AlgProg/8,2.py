class Polinômio:
    def __init__ (self, coeficientes):
        self.poli = coeficientes

    def __setitem__ (self, grau, coeficiente):
        if grau > len(self.poli):
            for i in range(grau - len(self.poli)):
                if i == range(grau - len(self.poli) - 1):
                    self.poli.append(coeficiente)
                else:
                    self.poli.append(0)
        else:
            self.poli[grau] = coeficiente

    def grau(self):
        return len(self.poli)

    def __add__(self, other):
        if self.grau() >= other.grau():
            self.poliadd = self.poli.copy()
            for i in range(other.grau()):
                self.poliadd[i] += other.poli[i]
        else:
            self.poliadd = other.poli.copy()
            for i in range(self.grau()):
                self.poliadd[i] += other.poli[i]
        return Polinômio(self.poliadd)

    def __sub__(self, other):
        self.polisub = other.poli.copy()
        for i in range(other.grau()):
            self.polisub[i] *= -1
            i += 1
        return self + Polinômio(self.polisub)

    def __mul__(self, other):
        self.polimult = [0] * (self.grau() + other.grau() - 1)
        for i in range(self.grau()):
            for j in range(other.grau()):
                self.polimult[i + j] += self.poli[i] * other.poli[j]
                j += 1
            i += 1
        return Polinômio(self.polimult)

    def avaliar(self, numero):
        f = 0
        for i in range(self.grau()):
            f += self.poli[i] * (float(numero) ** i)
        return f"{f:.2f}"

    def __repr__(self):
        return str(self.poli)

    def derivada(self):
        self.polideri = self.poli.copy()
        for i in range(self.grau()):
            self.polideri[i] *= i
        del self.polideri[0]
        return Polinômio(self.polideri)

    def raiz(self, x0, n):
        self.poliraiz = self.poli.copy()
        self.derivraiz = self.derivada().poli.copy()
        self.z = x0
        if n == 0:
            return f"{self.z:.2f}"
        else:
            try:
                self.z -= (float(self.avaliar(x0)) / float(self.derivada().avaliar(x0)))
                return self.raiz(self.z, n - 1)
            except ZeroDivisionError:
                return "Abortado"
        
    def integralr(self, a, b, n):
        dx = (b - a) / n
        self.retangular = 0
        for i in range(n):
            self.retangular += dx * float(self.avaliar((i * dx + (i + 1) * dx) / 2))
        return f"{self.retangular:.2f}"
    
    def integralt(self, a, b, n):
        dx = (b - a) / n
        self.trapézio = 0
        for i in range(n):
            self.trapézio += dx * (float(self.avaliar(i * dx))+ float(self.avaliar((i + 1) * dx))) / 2
        return f"{self.trapézio:.2f}"
    
In = eval(input())
f = Polinômio(In[0])
a, b, n = In[1], In[2], In[3]

print(f.integralr(a, b, n), f.integralt(a, b ,n))