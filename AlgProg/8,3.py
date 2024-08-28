class NumeroDecimal():
    def __init__(self, v):
        self.num = format(float(v), 'f')
        position = self.num.find(".")
        self.decimal = self.num[position + 1:]
        self.inteiro = self.num[:position]
        self.num = str(self.inteiro) + "," + str(self.decimal)

    def __add__(self, other):
        self.deciadd = int(self.decimal.copy())
        self.intadd = int(self.inteiro.copy())
        if len(str(self.deciadd)) > len(str(other.deciadd)):
            other.deciadd *= 10 ** len(str(self.deciadd) - len(str(other.deciadd)))
        else:
            self.deciadd *= 10 ** len(str(other.deciadd) - len(str(self.deciadd)))
        self.numadddecimal = self.deciadd + other.deciadd
        self.numaddinteiro = self.intadd + other.intadd
        if len(str(self.numadddecimal)) != len(str(self.numadddecimal)):
            self.numaddinteiro += 1
        self.numadd = str(self.numaddinteiro) + "," + str(self.numadddecimal)
        return NumeroDecimal(self.numadd)

    def __sub__(self, other):
        self.decisub = int(self.decimal.copy())
        self.intsub = int(self.inteiro.copy())
        if len(str(self.decisub)) > len(str(other.decisub)):
            other.decisub *= 10 ** len(str(self.decisub) - len(str(other.decisub)))
        else:
            self.decisub *= 10 ** len(str(other.decisub) - len(str(other.decisub)))
        if self.decisub < other.decisub:
                self.decisub += 10 ** len(str(self.decisub) + 1)
                self.intsub -= 1
        self.numsubdecimal = self.decisub - other.decisub
        self.numsubinteiro = self.intsub - other.intsub
        self.numsub = str(self.numsubinteiro) + "," + str(other.numsubinteiro)
        return NumeroDecimal(self.numsub)
    
    def __repr__(self):
        return self.num
    
print(NumeroDecimal(0.0000000000000000000000000000001))