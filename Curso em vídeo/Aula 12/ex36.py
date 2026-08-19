cs = float(input("Qual é o valor da casa? "))
s = float(input("Qual é o valor do seu salário? "))
p = float(input("Em quantas parcelas serão feitas ? "))
# dividir o valor da casa pela quantidade de parcelas e o valor da casa 
# não pode passar de 30% do salário se não é negada
parcelas = s / p
percentual = cs * 0.30
if p < percentual:
    print(f"O valor mensal da casa será de R$ {parcelas}")
else:
    print(f"A casa está indiponível pois irá atigir + 30% do seu salário")