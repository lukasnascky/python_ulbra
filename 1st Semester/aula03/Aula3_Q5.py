num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
cod = input("Código de condição: (c/d)\n>>>")

if cod == 'c':
    if num1 < num2:
        print(f"\nOrdem crescente: {num1}, {num2}")
    else:
        print(f"\nOrdem crescente: {num2}, {num1}")
elif cod == 'd':
    if num1 > num2:
        print(f"\nOrdem decrescente: {num1}, {num2}")
    else:
        print(f"\nOrdem decrescente: {num2}, {num1}")