pot = 2
num = int(input("Digite um valor: "))
if num >= 500:
    while num > 10:
        num = num / pot
        pot = pot * 2
else:
    print("Valor menor que 500!")

print("Última divisão:", num)