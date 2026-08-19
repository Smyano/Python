n = int(input("Digite um número "))
print('''Escolha uma opção para a conversão 
      1 - binário
      2 - octal
      3 - hexadecimal''')
op = int(input("sua opação: "))
if op == 1:
    print(f" o número {n} convertido para binário é {bin(n)}")
elif op == 2:
    print(f" o número {n} convertido para binário é {oct(n)}")
else:
    print(f" o número {n} convertido para binário é {hex(n)}")