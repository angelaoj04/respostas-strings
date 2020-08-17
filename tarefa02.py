nome = input("Informe seu nome: ")
nomeM = nome.upper()

print(nomeM)

print(nomeM[::-1])

lista = list(nomeM)
lista.reverse()

print("".join(lista))

