consumo = float(input("Consumo de água: (m³) >>> "))
tipo = input("Tipo do cliente: (r/c/i) >>> ")

if tipo == 'r':
    conta = 5.0 + (0.05 * consumo)
elif tipo == 'c':
    conta = 500
    if consumo > 80:
        conta += (consumo - 80) * 0.25
else:
    conta = 800
    if consumo > 100:
        conta += (consumo - 100) * 0.04

print(f"Conta: R${conta}")