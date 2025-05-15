import func

arquivo = 'estoque.json'
produtos = func.carregar_produtos(arquivo)

while True:
    menu = input('''
1. Registrar novo livro
2. Listar livros
3. Excluir livro
4. Pesquisar livro
5. Relatório de livros em estoque
0. Sair                                  
>>>''')
    if menu == '0':
        break
    
    elif menu == '1':
        dados = input("Insira os dados separados por vírgula:\nISBN, Título, Autor, gênero, preço de compra, preço de venda, quantidade disponível.\n>>>")
        isbn, titulo, autor, genero, p_compra, p_venda, qtd = dados.split(',')
        produtos[isbn] = {'titulo': titulo, 'autor': autor, 'genero': genero, 'preco de compra': p_compra, 'preco de venda': p_venda, 'quantidade':qtd}

        func.salvar_produto(arquivo, produtos)

    elif menu == '2':
        print("\nLista de livros:")
        func.lista_livros(arquivo)

    elif menu == '3':
        livro = input("\nDigite o ISBN do livro que deseja excluir: ")
        func.excluir_livro(arquivo, livro)

    elif menu == '4':
        livro = input("\nDigite o ISBN do livro que deseja excluir: ")
        func.pesquisa_livro(arquivo, livro)

    elif menu == '5':
        print("\nRelatório de livros fora de estoque:")
        func.relatorio_livros(arquivo)
        print("___fim___")

    else:
        print("Entrada inválida! Digite outro valor.")