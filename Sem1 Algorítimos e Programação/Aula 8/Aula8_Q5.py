preco_ing = 50
vendas = 120

while preco_ing > 30:
    lucro = (preco_ing * vendas) - 2000
    print("Preço ingresso:", preco_ing, "| Vendas:", vendas, "| Lucro:", lucro)
    preco_ing = preco_ing - 5
    vendas = vendas + 30