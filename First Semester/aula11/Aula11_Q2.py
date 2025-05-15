lista_num = []
num = int(input("Número: "))
while num != 0:
    lista_num.append(num)
    num = int(input("Número: "))
print("\nElementos:")
i = 0
while i < len(lista_num):
    print(lista_num[i])
    i = i + 1