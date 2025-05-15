import func

dicionario = func.carregar_dicionario('dicionario.json')

while True:
    menu = input('''
1. Cadastrar tradução
2. Traduzir frase | Inglê x Português
3. Traduzir frase | Português x Inglês
4. Exibir dicionário em ordem alfabética
5. Exibir maiores palavras
0. sair
>>> ''')
    
    if menu == '0':
        break

    elif menu == '1':
        palavra = input("\nDigite a palavra em inglês: ").lower()
        traducao = input("Digite sua tradução: ").lower()
        dicionario[palavra] = traducao
        func.salvar_dicionario('dicionario.json', dicionario)
        print("Tradução cadastrada com sucesso!")

    elif menu == '2':
        frase = input("\nDigite a frase que deseja traduzir: ").lower()
        frase_ingles = frase.split()
        for palavra in frase_ingles:
            frase.replace(dicionario[palavra],dicionario[])
        #print(func.traduzir_ingles_portugues(frase_ingles, dicionario))

    elif menu == '3':
        pass

    elif menu == '4':
        pass

    elif menu == '5':
        pass

    else:
        print("Opção inválida! Digite outro valor.")