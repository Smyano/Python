# k = float(input("Quantos KM foram percorridos? " ))
# km = k * 0.15
# d = float(input("Quantos dias foram utilizados? " ))
# dp = d * 60
# t = km + dp
# print(f"O valor total a ser pago é R$ {t:.2f}")

# ou>>>>>

k = float(input("Quantos KM foram percorridos? " ))
d = float(int("Quantos dias foram utilizados? " ))
t = k * 0.15 + (d * 60)
print(f"O total a pagar são R${t:.2f}")