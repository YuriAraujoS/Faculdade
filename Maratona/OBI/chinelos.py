N = int(input())
chinelos = []

for i in range(N):
    x = int(input())
    chinelos.append(x)

pedidos = int(input())
vendas = 0

for j in range(pedidos):
    y = int(input())
    if chinelos[y - 1] > 0:
        vendas += 1
        chinelos[y - 1] -= 1


print(vendas)