a = int(input("Digite a medida 1: "))
b = int(input("Digite a medida 2: "))
c = int(input("Digite a medida3: "))
if a + b > c and b + c > a and a + c > b: 
    print("Ok, podemos formar um triângulo")
else:
    print("Não podemos formar um triângulo")
if a == b == c:
    print("O triangulo é um equilátero")
elif a == b or a== c or c == b:
    print("O triangulo é um Isósceles")
else:
    print("O triangulo é um escalono")

     