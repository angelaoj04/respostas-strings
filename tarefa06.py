dataNascimento = input("Informe a data de nascimento no formato dd/mm/aaaa: ")

vetorData = dataNascimento.split("/")

vetorMeses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
              "agosto", "setembro", "outubro", "novembro", "dezembro"]
tamanho = len(vetorMeses)

imprimeData = ""
for i in range(0, tamanho):
    if(int(vetorData[1]) == (i+1)):
        myorder = "Você nasceu em {} de {} de {}"
        imprimeData = myorder.format(vetorData[0], vetorMeses[i], vetorData[2])

print(imprimeData)