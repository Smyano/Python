# f = input("Digite uma frase: ")

# for c in range(len(f)):
#     if f[c] == f(len(f) - 1 - c):
#         print(f"A frase / palavra {f} é palíndromo")
        
f = input("Digite uma frase: ")

for c in range(len(f)):
    if f[c] == f[len(f) - 1 - c]:
        print(f"A frase / palavra {f} é palíndromo")