import random
numeros = []
i = 0
while i < 10:
    numeros.append(random.randint(-5, 5))
    i = i + 1
print("Números:", numeros)
#MENOR VALOR NEGATIVO:
menor = 10
i = 0
while i < len(numeros):
    if numeros[i] < menor and numeros[i] < 0:
        menor = numeros[i]
    i = i + 1
print("Menor:", menor)
#ELEMENTOS NAS POSIÇÕES PARES
i = 0
while i < len(numeros):
    if i % 2 == 0:
        print(numeros[i])
    i = i + 1