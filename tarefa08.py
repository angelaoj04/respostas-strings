frase = input("Informe uma frase: ")

fraseSEspaco = frase.replace(" ", "")
vetorFrase = list(fraseSEspaco)
vetorFrase.reverse()

frase2 = ''.join(vetorFrase)

if frase2 == fraseSEspaco:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")


