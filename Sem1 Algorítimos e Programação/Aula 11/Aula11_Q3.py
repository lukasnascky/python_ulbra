lista = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50]
maior_num = 0
cont = 0
while cont < len(lista):
    if lista[cont] > maior_num:
        maior_num = lista[cont]
    cont = cont + 1
print("Maior elemento:", maior_num)
cont = 0
soma = 0
while cont < len(lista):
    if lista[cont] > 0:
        soma = soma + lista[cont]
    cont = cont + 1
print("\nSoma dos positivos:", soma)
print("\nPrimeiros 5 elementos:")
cont = 0
while cont < 5:
    print(lista[cont])
    cont = cont + 1
cont = 0
print("\nPosições:")
while cont < len(lista):
    if lista[cont] % 2 == 0:
        print(cont)
    cont = cont + 1