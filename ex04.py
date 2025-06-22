# O jeito qe estava sendo feito era, "print(D.isspace)", o D como a várival, porém 
# não havia o espaço pra o valor "isspace" ser validado, () e nem a mensagem onde iria retornar
# print ( D.isspace) -> feito desse jeito, significa que o ()excecuta a função após o final

D = (input("Digite algo "))
print (f"tipo primitivo dessa valor é {D}", type(D))
print ("Só tem espaços? ", D.isspace())
print ("Tem ao menos um espaços? ", " " in D)
print ("É númerico?", D.isnumeric())
print ("É alphanúmerico?", D.isalnum())
print ("Letras são minusculas?", D.islower())
print ("Letras são maiúsculos?", D.isupper())
