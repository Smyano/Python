frase = input("digite uma frase ")
print(f"""na frase {frase} a letra A aparecem {frase.count('a')} vezes
o primeiro A aparece na posição {frase.find('a')}
o ultimo A aparece na posição {frase.rfind('a')} """)
