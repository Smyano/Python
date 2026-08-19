n = int(input("Digite um número: "))
com_divisor = False


for c in range(2, n):
    if n % c == 0:
        com_divisor = True
    
    
if com_divisor == True:
    print(f"O número {n} não é primo")
else:
    print(f"O número {n} é primo")
    