import func

livros = func.carregar_livros('_livros.json')

while True:
    menu = input('''
    1. Registrar novo livro
    2. Listar livros
    3. Excluir livro
    4. Pesquisar livro
    5. Relatorio de livros sem estoque
    0. sair
    >>> ''')

    if menu == '0':
        break

    elif menu == '1':
        dados_livro = input("\nDigite os dados separados por vírgula: ISBN,titulo,autor,genero,preço de compra,preço de venda,quantidade\n>>> ")
        isbn, titulo, autor, genero, preco_compra, preco_venda, qtd = dados_livro.split(',')
        if isbn in livros:
            print("Este livro já está registrado!")
        else:
            livros[isbn] = {'titulo': titulo, 'autor': autor, 'genero': genero, 'preco_compra': preco_compra, 'preco_venda': preco_venda, 'qtd': qtd}
            func.salvar_livros('_livros.json', livros)
            print("Livro cadastrado com sucesso!")

    elif menu == '2':
        print("\n\tLista de livros disponíveis:\n" + "=" * 50)
        func.listar_livros(livros)

    elif menu == '3':
        livro_a_deletar = input("\nQual livro deseja deletar? Digite o ISBN\n>>> ")
        func.deletar_livro(livros, livro_a_deletar)
        func.salvar_livros('_livros.json', livros)
        print("Livro excluido com sucesso!")
    
    elif menu == '4':
        livro_a_pesquisar = input("\nDigite o título que deseja encontrar\n>>> ")
        func.pesquisar_livro(livro_a_pesquisar, livros)

    elif menu == '5':
        print("\n\tLivros fora de estoque")
        print("=" * 50)
        func.listar_livros_sem_estoque(livros)

    else:
        print("Opção inválida! Digite outro valor.")