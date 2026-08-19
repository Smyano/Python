# a soma dos dois lados precisa ser maior que o terceiro valor
a = int(input("Digite a medida 1: "))
b = int(input("Digite a medida 2: "))
c = int(input("Digite a medida 3: "))
if a + b > c and b + c > a and c + a > b:
    print("as medidas informadas tornam um triângulo")
else:
    print("As medidas informadas não podem tornar um triângulo")
