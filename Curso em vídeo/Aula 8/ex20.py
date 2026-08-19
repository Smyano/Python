# import random  
# a1 = str(input("Digte o primeiro nome "))
# a2 = str(input("Digte o segundo nome "))
# a3 = str(input("Digte o terceiro nome "))
# lista = [a1 , a2 , a3] 
# p, s, t = random.sample(lista, 3)

# print (f" \n Primeiro: {p} \n Segundo: {s} \n Terceiro: {t}")
 
import random
a1 = input("digite o nome do primeiro aluno ")
a2 = input("digite o nome do primeiro aluno ")
a3 = input("digite o nome do primeiro aluno ")
lista = [a1, a2, a3]
random.shuffle(lista) #shuffle serve para "bagunçar"
print(f"ordem será {lista}")
