i = 0
estoque = [['001', 'marmelada', 50, 6.50], ['002', 'goiabada', 20, 6.00], ['003', 'ambrosa', 25, 5.00], ['004', 'maria mole', 100, 5.50], ['005', 'brigadeiro', 55, 4.00]]
print('Insira os dados de um doce:')
#SOLICITA OS DADOS DE UM NOVO DOCE
while i < 1:
    doce = []
    doce.append(input("Código: "))
    doce.append(input("Nome do doce: "))
    doce.append(int(input("Quantidade: ")))
    doce.append(float(input("Preço: ")))
    estoque.append(doce)
    i = i + 1
#APRESENTA NOME E QUANTIDADE TOTAL DE CADA DOCE
i = 0
while i < len(estoque):
    print("\nDoce:", estoque[i][1], "\nValor total: R$", estoque[i][2]*estoque[i][3])
    i = i + 1
#COMPRA DO CLIENTE
i = 0
print("\nCOMPRA")
cod = input("Código do doce: ")
qtd = int(input("Quantidade: "))
while i < len(estoque):
    if cod == estoque[i][0]:
        if qtd <= estoque[i][2]:
            estoque[i][2] = estoque[i][2] - qtd
            print("Valor a pagar: R$", estoque[i][3]*qtd)
        else:
            print("Não há quantidade suficiente em estoque!")
    i = i + 1