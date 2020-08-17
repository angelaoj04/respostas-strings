string1 = "Sou professora"
string2 = "Sou professora"

print(string1, ", Comprimento: ", len(string1))
print(string2, ", Comprimento: ", len(string2))

if len(string1) == len(string2):
    print("As strings possuem o mesmo comprimento")
else:
    print("Comprimentos diferentes!")

if string1 == string2:
    print("Os textos são iguais")
else:
    print("Textos diferentes!")