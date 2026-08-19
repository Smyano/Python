# calcular a distancia de uma viagem
# 200 km por R$ 0,50 se for mais que 200 cobre 0,45
 
d = float(input("me diga a distancia da sua viagem: "))
df = 200
if d <= df:
    d1 = 0.50
    valor1 = d * d1
    print(f"O valor da sua viagem é {valor1}")
else:
    d2 = 0.45
    valor2 = d * d2
    print(f"O valor da sua viagem é {valor2}")