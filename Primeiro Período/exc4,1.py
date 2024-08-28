matriz = eval(input())
def det1():
    det = matriz[0]
    print(det)
def det2():
    det = (matriz[0][0] * matriz[1][1]) - (matriz [0][1] * matriz [1] [0])
    print(det)
def det3():
    det = matriz[0][0] * matriz[1][1] * matriz[2][2] - matriz[0][0] * matriz[1][2] * matriz[2][1] + matriz[1][0] * matriz[2][1] * matriz[0][2] + matriz[2][0] * matriz [0][1] * matriz[1][2] - matriz[1][0] * matriz[0][1] * matriz[2][2] - matriz[2][0] * matriz[1][1] * matriz[0][2]
    print(det)
if len(matriz) == 1: 
    det1()
if len(matriz) == 2: 
    det2()
if len(matriz) == 3: 
    det3()