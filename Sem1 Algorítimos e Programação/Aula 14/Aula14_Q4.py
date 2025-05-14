i = 0
numeros = []
while i < 3:
    numero = []
    numero.append(float(input("Primeiro número: ")))
    if (numero[0]) % 2 == 0:
        segundo = (numero[0]) / 2
    elif (numero[0]) % 2 != 0:
        segundo = (numero[0] * 2)
    print("Segundo número:", segundo)
    numero.append(segundo)
    terceiro = (numero[0]) * 3
    numero.append(terceiro)
    print("Terceiro número:", terceiro, "\n")
    numeros.append(numero)
    i = i + 1
print(numeros)
#_#