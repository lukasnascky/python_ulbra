cardapio = [['Cachorro-quente',5.00], ['X-Salada', 10.00], ['X-Bacon', 12.00], ['Bauru', 8.00], ['Refrigerante', 4.00], ['Suco', 6.00]]
print(cardapio)
continuar = input("Deseja fazer o pedido? s/n: ")
while continuar == "s":
    pedido = []
    item = int(input("Código do item desejado: "))
    qtd = int(input("Quantidade do item desejado: "))
    
    continuar = input("Continuar pedindo? s/n: ")