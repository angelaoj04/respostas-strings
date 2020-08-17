frase = input("Informe uma frase: ")
espaco = " "
cont = 0
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

for i in range(0, len(frase)):
    if(espaco in frase[i]):
        cont = cont + 1
    if("a" in frase[i] or "A" in frase[i]):
        contA = contA + 1
    if("e" in frase[i] or "E" in frase[i]):
        contE = contE + 1
    if("i" in frase[i] or "I" in frase[i]):
        contI = contI + 1
    if("o" in frase[i] or "O" in frase[i]):
        contO = contO + 1
    if("u" in frase[i] or "U" in frase[i]):
         contU = contU + 1

print("Espaços em branco: ",cont)
print("Quantidade de a ou A: ",contA)
print("Quantidade de e ou E: ",contE)
print("Quantidade de i ou I: ",contI)
print("Quantidade de o ou O: ",contO)
print("Quantidade de u ou U: ",contU)