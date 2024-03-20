def inverter(string):
    invert = ''
    tam = len(string)
    for i in range(tam - 1, -1, -1):
        invert += string[i]
    return invert

text = str(input("Digite um texto para inversão: "))
print("String original:", text)
print("String invertida:", inverter(text))
