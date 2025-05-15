import funcoes

arquivo = 'produtos.json'
produtos = funcoes.carregar_produtos(arquivo)

while True:
    dados = input("Cadastre um produto: codigo,nome (0 - sair): ")
    if dados == "0":
        break
    codigo, nome = dados.split(',')
    produtos[codigo] = {'nome': nome}

funcoes.salvar_produtos(arquivo, produtos)