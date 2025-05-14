cont = 0
qtd_branco = 0
qtd_tinto = 0
qtd_rose = 0

while cont < 50:
    tipo = input("Tipo do vinho:(b - branco, t - tinto, r - rosê) ")
    if tipo == "b":
        qtd_branco = qtd_branco + 1
    elif tipo == "t":
        qtd_tinto = qtd_tinto + 1
    elif tipo == "r":
        qtd_rose = qtd_rose + 1
    else:
        print("Não existe!")
    cont = cont + 1
per_branco = (qtd_branco / cont) * 100
per_tinto = (qtd_tinto / cont) * 100
per_rose = (qtd_rose / cont) * 100
print("Percentual Vinho Branco:", per_branco)
print("Percentual Vinho Tinto:", per_tinto)
print("Percentual Vinho Rosê:", per_rose)

#testar depois!!!!!