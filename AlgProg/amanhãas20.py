A = "Sábado às 20:00h no Gurumê?"
B = "Digite 's' se sim e 'n' se não"
print (A)
print (B)
R = input("Resposta: ")
def res (R):
    if R == "s":
        return "Aeeeeee! Te vejo lá ;)"
    elif R == "n":
        print("Resposta errada, tente novamente :(")
        print(A)
        print(B)
        r = input("Resposta: ")
        return (res(r))
print(res(R))