class Matriz:
    def __init__(self, n, m, v):
        self.n, self.m = int(n), int(m)
        self.M = []
        self.v = v
        for i in range(self.n):
            l = []
            for j in range(self.m):
                l.append(v[j + i * self.m])
                j += 1
            self.M.append(l)
            i += 1
    def __add__(self, other):
        self.vadd = []
        for i in range(self.n + self.m):
            self.vadd.append(self.v[i] + other.v[i])
            i+= 1
        return Matriz(self.m, self.n, self.vadd)
    def __sub__(self, other):
        self.vsub = []
        for i in range(self.n + self.m):
            self.vsub.append(self.v[i] - other.v[i])
            i += 1
        return Matriz(self.m, self.n, self.vsub)
    def __mul__(self, other):
        self.vmult = []
        p = 0
        for i in range(self.n):
            for j in range(other.m):
                elemento = 0
                for k in range(self.m):
                    elemento += self.v[p + k] * other.v[j + k * other.m]
                    k += 1
                self.vmult.append(elemento)
                j += 1
            p += self.m
            i += 1
        return Matriz(self.n, other.m, self.vmult)
    def __repr__(self):
        return str(self.M)
    #def transp(self):
    #    self.vmult = []
    #    for i in range(self.n):
    #        p = 0
    #        for j in range(other.m):
    #            elemento = 0
    #            for k in range(self.m):
    #                o = i + k * other.m
    #                print(self.v[o], other.v[p + k], elemento)
    #                elemento += self.v[o] * other.v[p + k]
    #                k += 1
    #                print(self.vmult)
    #            self.vmult.append(elemento)
    #            p += self.m
    #            j += 1
    #    i += 1

#def receber(entrada):
#    fim = entrada.find(')')
#    i = entrada[fim + 1]
#    x, y = str(entrada).split(i, 1)
#    val1 = eval(x)
#    val2 = eval(y)
#    x = Matriz(val1[0], val1[1], val1[2])
#    y = Matriz(val2[0], val2[1], val2[2])
#    if i == '+':
#        return x + y
#    elif i == '-':
#        return x - y
#    else:
#        return x * y

print(Matriz(2, 2, [1,2,3,4]) * Matriz(2, 2, [1,2,3,4]) * Matriz(2, 2, [1,2,3,4]))