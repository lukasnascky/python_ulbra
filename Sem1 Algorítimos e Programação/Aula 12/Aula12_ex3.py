import random
numeros = []
i = 0
while i < 10:
    numeros.append(random.randint(1, 50))
    i = i + 1
print("Números:", numeros)
#APRESENTAÇÃO DOS 5 PRIMEIROS
i = 0
print("\nPrimeiros 5 valores:")
while i < 5:
    print(numeros[i])
    i = i + 1
#SOMA DOS ELEMENTOS NAS POSIÇÕES PARES
soma = 0
i = 0
while i < len(numeros):
    if i % 2 == 0:
        soma = soma + numeros[i]
    i = i + 1
print("\nSoma:", soma)
#MENOS DOS 3 ULTIMOS ELEMENTOS
menor = 51
i = len(numeros) - 1
while i >= len(numeros) - 3:
    if numeros[i] < menor:
        menor = numeros[i]
    i = i - 1
print("\nMenor:", menor)