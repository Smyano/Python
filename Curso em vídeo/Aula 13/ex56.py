idade = 0
midade = 0
maiorIH = 0
nmaisvelho = ""
for c in range (1,5):
    print(f"Dados da pessoa {c}")
    n = input("Nome: ")
    i = int(input("Idade: "))
    s = input("Sexo F ou M? ")
    idade += i
    if c ==1 and s in "Mm":
        maiorIH = i
        nmaisvelho = n
    if s in "Mm" and i > maiorIH:
        maiorIH = i
        nmaisvelho = n
midade = idade / 4
print(f"A média da idade do grupo é de {midade}")
print(f"O mais velho tem {maiorIH} anos e se chama {nmaisvelho}")
    
    