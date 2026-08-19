nome = str(input("Digite o seu nome completo: ")) #usuário digita nome
nc = nome.replace(' ','') #separa os espaços #conta a variavel separada pelos espaçõs
c = nome.split() #conta o nome em fatiamento
print(f"""seu nome em mínusculo: {nome.lower()}  
seu nome em maíusculo: {nome.upper()}
seu nome têm {len(nc)} caracteres (sem contar os espaços) 
seu primeiro nome têm {len(c[0])} letras""")
