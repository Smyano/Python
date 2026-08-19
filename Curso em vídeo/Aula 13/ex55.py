maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f"Peso da pessoa {c}: ")) 
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"O maior peso foi de {maior} kg e o menor peso foi de {menor} kg") 
