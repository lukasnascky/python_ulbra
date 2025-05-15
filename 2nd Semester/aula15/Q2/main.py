import func

nome_arquivo_entrada = 'usuarios.txt'
nome_arquivo_saida = 'relatorio.txt'

usuarios = func.ler_arquivo(nome_arquivo_entrada)

while True:
    print('''Escolha uma opção:
1. Gerar relatório completo
2. Gerar relatório com os top N usuários
0. Sair''')
    
    menu = input(">>> ")
    
    if menu == '0':
        break
    elif menu == '1':
        func.gerar_relatorio(usuarios, nome_arquivo_saida)
        print(f'Relatório completo gerado em {nome_arquivo_saida}')
    elif menu == '2':
        top_n = input("Digite o número de usuários a serem exibidos no relatório: ")
        top_n = int(top_n)  
        func.gerar_relatorio(usuarios, nome_arquivo_saida, top_n)
        print(f'Relatório com os top {top_n} usuários gerado em {nome_arquivo_saida}')
    else:
        print("Opção inválida. Tente novamente.")