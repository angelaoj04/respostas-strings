nome = input("Informe seu nome: ")

tamanho = len(nome)

resposta = ""

for i in range(0, tamanho):
    resposta = resposta + nome[i]
    print(resposta)
