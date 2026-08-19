a = 2018
id = 18
i = int(input("Digite seu ano de nascimento "))
idade = a - i
if idade == 18:
    print("Está na hora de se alistar no serviço militar ")
elif idade > 18:
    print(f"Já passou da hora de se alistar no serviço militar, fazem {idade - id} ano(s) atrás")
else:
    print(f"Ainda não é a hora de se alistar no serviço militar, faltam {id - idade} ano(s) ainda")
