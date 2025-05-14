num = []
i = 0
while i < 10:
    num.append(float(input("Valor: ")))
    i = i + 1
print("Números:", num)
#TROCA DOS 5 PRIMEIROS PELO SEU DOBRO
i = 0
while i < 5:
    num[i] = num[i] * 2
    i = i + 1
print("\nNúmeros:", num)
#TROCA DOS 5 ULTIMOS PELA SUA METADE
while i > 5:
    num[i] = num[i] / 2
    i = i + 1
print("\nNúmeros:", num)