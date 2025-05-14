#CRIA LISTAS ALEATÓRIAS
import random
lista1 = []
lista2 = []
c = 0
while c < 20:
    lista1.append(random.randint(-5, 5))
    lista2.append(random.randint(-5, 5))
    c = c + 1
print("Lista1:", lista1)
print("Lista2:", lista2)
#MÉDIA DOS ELEMENTOS POSITIVOS DA LISTA
i = 0
soma = 0
elementos = 0
while i < len(lista1):
    if lista1[i] > 0:
        soma = soma + lista1[i]
        elementos = elementos + 1
    i = i + 1
media = soma / elementos
print("\nMédia dos positivos da lista 1:", media)
#QUANTAS VEZES O ULTIMO ELEMENTO SE REPETE NA LISTA 2
i = 0
ultimo = 0
while i < len(lista2):
    if lista2[i] == lista2[-1]:
        ultimo = ultimo + 1
    i = i + 1
print("\nO último elemento se repetiu", ultimo, "vezes!")
#SOLICITA POSIÇÃO E IMPRIME VALOR INDICADO NA LISTA 2, SEU ANTECESSOR E SEU SUCESSOR
posicao = int(input("\nDigite uma posição: "))
print("Número solicitado: ", lista2[posicao])
print("Antecessor: ", lista2[posicao - 1])
print("Sucessor: ", lista2[posicao + 1])
#LISTA COM VALORES IGUAIS NAS MESMAS POSIÇÕES NAS DUAS LISTAS
i = 0
lista3 = []
while i < len(lista1):
    if lista1[i] == lista2[i]:
        lista3.append(lista1[i])
    i = i + 1
if len(lista3) < 1:
    print("\nNão há números nas mesmas posições nas duas listas!")
else:
    print("\nNúmeros na mesma posição em ambas as listas:", lista3)
#_#