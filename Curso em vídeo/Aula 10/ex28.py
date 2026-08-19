# ne = 3
# n = int(input("Digite o número que eu escolhi de 0 à 5: "))
# if n == ne:
#     print(f"Parabéns o número escolhido foi {ne}")
# else:
#     print(f"Resposta errada, não foi o número {n}, o número escolhido foi {ne}")

from random import randint
c = randint(0,5)
print("Adivinhe o número que eu pensei entre 0 e 5")
n = int(input("Digite um número: "))
if n == c:
    print(f"Parabéns o número escolhido foi o {c}")
else:
    print(f"Que pena! O número escolhido foi {c} e não {n}")
