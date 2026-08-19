# Em Python, ANSI normalmente significa usar códigos de escape ANSI para mudar cor, estilo e fundo do texto no terminal.

# Estrutura:
#     \033[estilo;cor_texto;cor_fundo m
# O \033[ inicia o código ANSI.
# O 31m define a cor vermelha.
# O \033[m reseta a formatação para o padrão.

# Cores principais do texto
# 30 = preto
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = roxo/magenta
# 36 = ciano
# 37 = branco

# Estilos
# 0 = normal
# 1 = negrito
# 4 = sublinhado
# 7 = negativo/invertido

# Fundo
# 40 = fundo preto
# 41 = fundo vermelho
# 42 = fundo verde
# 43 = fundo amarelo
# 44 = fundo azul
# 45 = fundo roxo/magenta
# 46 = fundo ciano
# 47 = fundo branco

print("\033[35m Olá, mundo!")
