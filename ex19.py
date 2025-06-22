import random  
a1 = str(input("Digte o primeiro nome "))
a2 = str(input("Digte o segundo nome "))
a3 = str(input("Digte o terceiro nome "))
lista = [a1 , a2 , a3]
e = random.choice(lista)
print(f"O aluno escolhido foi {e}")
