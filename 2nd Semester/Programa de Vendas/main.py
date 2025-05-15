import func

vendas = func.carregar_algo('vendas.json')

while True:
    func.limpar_terminal()
    menu = input('''1. Registrar venda
2. Gerar relatório diário
3. Gerar relatório mensal
0. sair
>>> ''')
    if menu == '0':
        break

    elif menu == '1':
        carrinho = func.carregar_algo('carrinho.json')
        while True:
            func.limpar_terminal()
            total_a_pagar = 0
            if carrinho:
                for item, info in carrinho.items():
                    print(f"Item: {item} | Preço: R${info['valor_item']} | Quantidade: {info['qtd_item']} | Valor a pagar: R${info['valor_a_pagar']}")
                    total_a_pagar += info['valor_a_pagar']
                print(f"Total a pagar: R${total_a_pagar}")
                
            else:
                print("Nada no carrinho!")
            
            menu_carrinho = input("\n1. Adcionar item\n2. Remover item\n0. Finalizar\n>>> ")
            if menu_carrinho == '0':
                break
            
            elif menu_carrinho == '1':
                item = input("\nItem: ")
                valor_item = float(input("Valor: "))
                qtd_item = int(input("Quantidade: "))
                valor_a_pagar = valor_item * qtd_item
                carrinho = func.adciona_ao_carrinho(carrinho, item, valor_item, qtd_item, valor_a_pagar)
            
            elif menu_carrinho == '2':
                item_a_remover = input("\nItem para remoção: ")
                func.remover_do_carrinho(carrinho, item_a_remover)

            else:
                print("\nOpção inválida! \nPor favor digite outro valor.")
        

    elif menu == '2':
        pass

    elif menu == '3':
        pass

    else:
        print("\nOpção inválida! \nPor favor digite outro valor.")