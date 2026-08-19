# programa que leia 3 número mostrando o maior e o menor

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 < n2 > n3:
    print(f"o número maior é o {n2} e o menor é {n1}")

elif n2 < n3 and n1:
    print(f"o número maior é o {n3} e o menor é {n2}")

elif n3 < n1 and n2:
    print(f"o número maior é o {n1} e o menor é {n3}")



