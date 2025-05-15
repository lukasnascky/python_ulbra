import func

arquivo = 'traducoes.json'
traducoes = func.carregar_traducoes(arquivo)

while True:
    menu = input('''
1. Cadastrar tradução
2. Traduzir frase inglês x português
3. Traduzir frase português x inglês
4. Exibir dicionário em ordem alfabética
5. Exibir maiores palavras
>>>''')

    if menu == '0':
        break

    elif menu == '1':
        palavra = input("\nPalavra: ")
        traducao = input("Tradução: ")
        traducoes[palavra.lower()] = traducao.lower()

        func.salvar_traducao(arquivo, traducoes)

    elif menu == '2':
        frase = input("\nDigite a frase a ser traduzida: ")
        print(func.traduz_ingles_portugues(arquivo, frase))

    elif menu == '3':
        frase = input("\nDigite a frase a ser traduzida: ")
        print(func.traduz_portugues_ingles(arquivo, frase))

    elif menu == '4':
        print("Dicionário em ordem alfabética: ")
        func.dicionario_ordem_alfabetica(arquivo)

    elif menu == '5':
        print("\nMaiores palavras do dicionario:")

    else:
        print("\nEntrada inválida! Digite outro valor.")