litros = float(input("Quantidade abastecida: (litros) >>> "))
tipo = input("Tipo de combustível: (a/g) >>> ")

if tipo == 'g':
    total = 7.0 * litros
elif tipo == 'a':
    total = 5.0 * litros


if total >= 20 and total <= 30:
    valor_a_pagar = total - (total * 0.05)
elif total > 30:
    valor_a_pagar = total - (total * 0.1)
else:
    valor_a_pagar = total

print(f"\nValor a pagar: R${valor_a_pagar}")