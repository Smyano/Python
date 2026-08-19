# salario maior que 1.2500 com aumento de 10% menor do que isso aumento de 15%
s = float(input("Digite o seu salário: "))
if s > 12.500:
    aumento1 = s * 0.15
    print(f"Seu salário atual será de R$ {aumento1 + s}")
else:
    aumento2 = s * 0.10
    print(f"Seu salário atual será de R$ {aumento2 + s}")