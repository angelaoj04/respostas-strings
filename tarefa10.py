numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
final = ''

num = int(input("Informe o número: "))

if num >= 0 and num < 20:
    print(f"O número que voce digitou é {numeros[num]}")
elif num >= 20 and num < 100:
    divisao = num//10
    resto = num%10
    print(f"Número que você digitou: {dezenas[divisao-2]} e {numeros[resto]}")
else:
    print("Você precisa digitar um número entre 0 e 99!")