maiores = 0 
menores = 0
for c in range(1,8):
 
    i = int(input(f"Digite a idade {c}: ")) 
    if i >= 18:
        print("Maior de idade")
        maiores +=1

    else:
        print("Menor de idade")
        menores +=1
print(f"O total de menores de idade são {menores}")
print(f"O total de maiores de idade são {maiores}")

