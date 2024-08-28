class Intervalo:
    def __init__(self, a, b):
        if float(b) < float(a):
            self.intervalo = [float(b), float(a)]
        else:
            self.intervalo = [float(a), float(b)]
    def interseção(self, other):
        if self.compreendido(other) == True:
            if self.intervalo[0] <= other.intervalo[0]:
                if self.intervalo[0] <= other.intervalo[0] <= self.intervalo[1]:
                    if other.intervalo[1] <= self.intervalo[1]:
                        return Intervalo(other.intervalo[0], other.intervalo[1])
                    else:
                        return Intervalo(other.intervalo[0], self.intervalo[1])
                else:
                    raise ValueError
            else:
                if other.intervalo[0] <= self.intervalo[0] <= other.intervalo[1]:
                    if self.intervalo[1] <= other.intervalo[1]:
                        return Intervalo(self.intervalo[0], self.intervalo[1])
                    else:
                        return Intervalo(self.intervalo[0], other.intervalo[1])
                raise ValueError
        else:
            raise ValueError
    def união(self, other):
        if self.compreendido(other) == True:
            if self.intervalo[0] <= other.intervalo[0]:
                if self.intervalo[0] <= other.intervalo[0] <= self.intervalo[1]:
                    if other.intervalo[1] <= self.intervalo[1]:
                        return Intervalo(self.intervalo[0], self.intervalo[1])
                    else:
                        return Intervalo(self.intervalo[0], other.intervalo[1])
                else:
                    raise ValueError
            else:
                if other.intervalo[0] <= self.intervalo[0] <= other.intervalo[1]:
                    if self.intervalo[1] <= other.intervalo[1]:
                        return Intervalo(other.intervalo[0], other.intervalo[1])
                    else:
                        return Intervalo(other.intervalo[0], self.intervalo[1])
                raise ValueError
        else:
            raise ValueError
    def compreendido(self, other):
        if self.intervalo[0] >= other.intervalo[0]:
            if self.intervalo[1] >= other.intervalo[1]:
                return True
            else:
                return False
        else:
            if other.intervalo[1] <= self.intervalo[1]:
                return True
            else:
                return False

    def __repr__(self):
        return "Intervalo" + str(tuple(self.intervalo))
    
def adiciona(l, i):
    for k in range(len(l)):
        try:
            x = i.união(l[k])
            l.append(x)
            del l[k]
            return adiciona(l, x)
        except:
            pass
        if k == len(l) - 1:
            return l

e1, e2, e3, e4 = eval(input())
l = [Intervalo(e1[0],e1[1]), Intervalo(e2[0], e2[1]), Intervalo(e3[0], e3[1])]

l = print(adiciona(l, Intervalo(e4[0], e4[1])))

#((4,1),(10,2),(2,10),((5,6),(7,9)))
#((4.1,1),(9.5,5),(6,10),((-1,0),(3,5)))
