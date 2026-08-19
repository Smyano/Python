# p = float(input("Digite o valor do produto: "))
# pgto = int(input("""
# ---Opções de pagamentos---\n
# 1 - À vista, dinheiro ou cheque (10% de desconto)
# 2 - Cartão á vista (5% de desconto)
# 3 - 2X no cartão
# 4 - 3x ou mais no cartão (20% de juros)\n
# Qual é o condição de pagamento? """))
# if pgto == 1:
#     print(f"O valor a pagar é R$ {p - 0.10:.2f}")
# elif pgto == 2:
#     print(f"O valor a pagar é R${0.5 - p:.2f}")
# elif pgto == 3:
#     print(f"o valor do pagamento é R$ {p:.2f}")
# else:
#     print(f"O valor do pagamento é R$ {p * 0.20:.2f}")

p = float(input("Informe o valor do produto: "))
print("""\nCondições de pagamentos:\n 
1 - Pagamento à vista
2 - Pagamento no cartão à vista
3 - Pagamento em 2x no cartão
4 - Pagamento no cartão parcelado 3x ou mais \n""")
opcao = int(input("Qual a opção de pagamento? "))
if opcao == 1:
    t = p - (p * 10 / 100)
    print(f"O valor do produto é R$ {t:.2f}")
elif opcao == 2:
    t = p - (p * 5 / 100)
    print(f"O valor do produto é R$ {t:.2f}")
elif opcao == 3:
    print(f"O valor do produto é R$ {p/2:.2f}")
elif opcao == 4:
   t  = p + (p* 20/100)
   parc = int(input("Quantas parcelas serão feitas? "))
   parcela = t / parc
   print(f"""Sua compra será parcelada em {parc}x, sendo assim o valor por parcela será de {parcela:.2f}, sendo o total de {t}""")
else:
    print("A opção escolhida deve ser de 1 à 4.")