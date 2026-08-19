km = int(input("Quantos km/h seu carro está? "))
if km <=80:
    print("Ok, está conforme a lei")
else:
    limite = 80
    multa = (km) - 80
    mf= 7 * multa
    print(f"Você está multado, no valor de R$ {mf}")