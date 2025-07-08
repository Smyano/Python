nome = str(input("Digite o seu nome completo: "))
nome.lower()
nome.upper()
nc = nome.replace(' ','')
len(nc)
cont = nome.split()
len(cont[0])
print(f"""seu nome em mínusculo: {nome.lower()}  
seu nome em maíusculo: {nome.upper()}
seu nome têm {len(nc)} caracteres (sem contar os espaços)
seu primeiro nome têm {len(cont[0])} letras""")