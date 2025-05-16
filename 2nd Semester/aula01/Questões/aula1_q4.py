valor_produto = float(input("Valor Produto: R$"))

valor_com_desconto = valor_produto - (valor_produto * .1)

print(f"Valor com desconto: R${valor_com_desconto:.2f}")