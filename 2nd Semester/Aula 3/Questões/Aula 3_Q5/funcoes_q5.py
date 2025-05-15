def verifica_categoria(nome, sal_min, qtd_camisetas):
    valor_recebido = sal_min + (qtd_camisetas * 0.5)
    if valor_recebido <= 1000:
        categoria = "A"
    elif valor_recebido <= 1500:
        categoria = "B"
    elif valor_recebido <= 2000:
        categoria = "C"
    else:
        categoria = "D"
    return f"\nVendedor: {nome}\nCategoria: {categoria}\nValor recebido: R${valor_recebido}\n"