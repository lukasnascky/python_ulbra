lista = []
cont = 0
while cont < 9:
    lista.append(int(input("Digite um valor inteiro: ")))
    cont = cont + 1
x = int(input("Digite um valor inteiro: "))
lista.append(lista[0])
lista[0] = x
print(lista)