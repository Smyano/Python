n = float(input("qual o valor do produto? R$"))
n1 = ((n / 100) * 5)
n2 = n - n1
print(f"O valor com 5% de desconto é R${n2:.2f}")