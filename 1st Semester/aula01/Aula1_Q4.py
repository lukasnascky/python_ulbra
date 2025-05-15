salario_minimo = float(input("Valor do Salário Mínimo: R$ "))
qtd_quilowatts = float(input("Quantidade de quilowatts gasta: "))

valor_a_pagar = (salario_minimo * 0.01) * qtd_quilowatts

print(f"\nValor a pagar: R$ {valor_a_pagar}")