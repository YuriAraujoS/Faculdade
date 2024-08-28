x  = int(input())
y = int(input())
i = 0
def div_inteira():
    global x, y, i
    if x >= y:
        x -= y
        i += 1
        return div_inteira()
    else:
        return i
print(div_inteira())