P = int(input())
D = int(input())
B = int(input())

sum = P + 2*D + 3*B

if sum < 100:
    print("N")
elif 100 <= sum < 120:
    print("P")
elif 120 <= sum < 150:
    print("D")
else:
    print("B")  




    