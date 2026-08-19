a = float(input("Digite sua altura: "))
p = float(input("Digite o seu peso: "))
imc = p/ (a * a) 
print(f"Seu imc é {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc <= 24:
    print("Você está no peso ideal")
elif imc <= 30:
    print("Você está com sobrepeso")
elif imc <= 40:
    print("Você está com obsidade")
else:
    print("Você está com obsidade mórbida")