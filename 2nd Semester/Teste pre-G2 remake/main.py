import func

arquivo = 'traducoes.json'
dicionario = func.carregar_traducoes(arquivo)

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
        dicionario[palavra.lower()] = traducao.lower()

        func.salvar_traducao(arquivo, dicionario)

    elif menu == '1':
        pass

    elif menu == '1':
        pass

    elif menu == '1':
        pass

    elif menu == '1':
        pass

    else:
        print("\nEntrada inválida! Digite outro valor.")
