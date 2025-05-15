lista_num = []
cont = 0
while cont < 6:
    num = int(input("Número: "))
    lista_num.append(num)
    cont = cont + 1
print("Elementos: ")
cont = 0
while cont < 6:
    print(lista_num[cont])
    cont = cont + 1
cont = 0
while cont < 6:
    print(lista_num[cont])
    cont = cont + 1
soma = 0
p = 0
while p < len(lista_num):
    if lista_num[p] % 2 == 0:
        soma = soma + lista_num[p]
    p = p + 1
print(soma)