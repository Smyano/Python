a = int(input("Digite um ano: "))
if a % 400 == 0:
    print(f"Ano {a} é bissexto")
elif a % 100 == 0:
    print(f"Ano {a} não é bissexto")
elif a % 4 == 0:
    print(f"Ano {a} não é bissexto")
else:
    print(f"Ano {a} não é bissexto")

