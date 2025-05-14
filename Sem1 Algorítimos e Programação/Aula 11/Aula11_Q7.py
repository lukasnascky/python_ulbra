lista = [-5, 10, -8, -3, 5, 10, 11, 8, -9, 10]
positivos = []
negativos = []
cont = 0
while cont < len(lista):
    if lista[cont] < 0:
        negativos.append(lista[cont])
    elif lista[cont] > 0:
        positivos.append(lista[cont])
    cont = cont + 1
print("Positivos:", positivos)
print("Negativos:", negativos)