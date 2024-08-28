a = int(input())
b = int(input())
c = int(input())
delta = (b ** 2 - 4 * a * c)

if delta >= 0:

    x1 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / 2 * a
    x2 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / 2 * a

    if x1 == x2:
        print(x1)
    else:
        print(x1, x2)

else:
    print("Não existem raízes reais")