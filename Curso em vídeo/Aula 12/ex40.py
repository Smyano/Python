n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
m = (n1 + n2) /2
if m >=7:
    print("Parabens! Você foi aprovado")
elif m <=5:
    print("Você foi reprovado")
else: #m == 6 and 5:
    print("Você está de recuperação")
