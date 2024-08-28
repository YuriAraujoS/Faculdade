n = int(input())
def f_lazy_fibonacci():
    a = 0
    b = 1
    x = 0
    for k in range(n):
        yield x
        x = a + b
        if k == 0:
            yield x
        a = b
        b = x
for i, x in enumerate(f_lazy_fibonacci()):
    if i >= n:   break
    print(x,end=' ')