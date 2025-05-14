import random
lista = []
i = 0
while i < 20:
    lista.append(random.randint(20, 30))
    i = i + 1
print(lista)
#SOMA DOS PRIMEIROS 10 VALORES
i = 0
soma = 0
while i < 10:
    soma = soma + lista[i]
    i = i + 1
print("\nSoma dos 10 primeiros:", soma)
#DIFERENÇA ENTRE O MAIOR E O MENOR NUMERO
i = 0
maior_num = 0
menor_num = 40
while i < len(lista):
    if lista[i] > maior_num:
        maior_num = lista[i]
    if lista[i] < menor_num:
        menor_num = lista[i]
    i = i + 1
diferenca = maior_num - menor_num
print("\nMaior número:", maior_num, "\nMenor número:", menor_num)
print("Diferença entre os dois:", diferenca)
#POSIÇÕES QUE O ULTIMO ELEMENTO APARECE
ult_elemento = []
i = 0
while i < len(lista):
    if lista[i] == lista[-1]:
        ult_elemento.append(i)
    i = i + 1
print("\nAparições do último elemento:", ult_elemento)
#POSIÇÃO SOLICITADA
solicitado = int(input("\nDigite uma posição: "))
print("Número na posição solicitada:", lista[solicitado])
#_#