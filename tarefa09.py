def validaFormato(cpf):
    if(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
        return False
    else:
        return True

def validaDigitos(cpf):
    cont = 10
    calculo = 0
    cpfNumeros = cpf.replace(".", "").replace("-", "")

    for i in range(0, 9):
        calculo = (int(cpfNumeros[i]) * (cont - i)) + calculo

    digito1 = (calculo * 10) % 11

    calculo = 0
    cont = 11
    for i in range(0, 10):
        calculo = (int(cpfNumeros[i]) * (cont - i)) + calculo

    digito2 = (calculo * 10) % 11

    if (digito1 != int(cpfNumeros[9])):
        return False
    elif digito2 != int(cpfNumeros[10]):
        return False
    else:
        return True

cpf = input("CPF(xxx.xxx.xxx-xx): ")

if(validaFormato(cpf)):
    print("O 'CPF' está no formato correto")
else:
    print("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")

if(validaDigitos(cpf)):
    print("O 'CPF' é válido!")
else:
    print("O CPF é inválido!")