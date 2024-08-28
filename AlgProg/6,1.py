A = eval(input())
B = eval(input())
i = 0
def testador():
    global i
    if B[i] == A[i]:
        return True
    else:
        i += 1
        if i != len(A) or i != len(B):
            return testador()
        else:
            return False
print(testador())