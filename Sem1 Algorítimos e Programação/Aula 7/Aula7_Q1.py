cont = 0
zero = 0
pos = 0
neg = 0
negcont = 0

while cont < 6:
    valor1 = int(input("Digite um valor:"))
    if valor1 > 0:
        print("Número positivo!\n")
        pos = pos + valor1
    elif valor1 < 0:
        print("Número negativo!\n")
        neg = neg + valor1
        negcont = negcont + 1
    else:
        print("Zero!\n")
        zero = zero + 1
    cont = cont + 1
print("Foram digitados", zero, "zeros!")
print("Soma dos valores positivos:", pos)
print("Média dos valores negativos:", neg / negcont)