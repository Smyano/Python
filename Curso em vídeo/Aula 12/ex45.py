from random import randint
jogador = int(input("""Escolha uma das opções abaixo:
1 - pedra
2 - papel
3 - tesoura
 """))
maquina = randint(1,3)
print(f"A máquina escolheu {maquina}")
if jogador == maquina:
    print("O jogo deu empate")
elif jogador == 1 and maquina == 2 or jogador == 3 and maquina == 1:
    print("Você perdeu")
else:
    print("Parabéns, você ganhou")

