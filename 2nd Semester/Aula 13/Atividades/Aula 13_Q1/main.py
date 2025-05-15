produtos = open("produtos.txt", "r")
produtos_lista = produtos.read().splitlines()
produtos.close()

em_estoque = open("emestoque.txt", "w")
fora_de_estoque = open("foradeestoque.txt", "w")

for produto in produtos_lista[1:]:
    condicao = produto.split(",")
    if condicao[1].strip().lower() == "sim":
        em_estoque.write(condicao[0] + "\n")
    else:
        fora_de_estoque.write(condicao[0] + "\n")

em_estoque.close()
fora_de_estoque.close()