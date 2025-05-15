from funcoes_q2 import *
cardapio =   [['Cachorro-quente',5.00],
              ['X-Salada', 10.00],
              ['X-Bacon', 12.00],
              ['Bauru', 8.00],
              ['Refrigerante', 4.00],
              ['Suco', 6.00]]
i = 0
print("------Cardápio------")
while i < len(cardapio):
    print(f"{cardapio[i][0]} - R${cardapio[i][1]}")
    i = i + 1

conta = ""
pedido_total = 0
while conta != "s":
    cod = int(input("\nCódigo: "))
    if cod > len(cardapio) or cod < 0:
        print("Código inválido")
    else:
        qtd = int(input("Quantidade: "))
        pedido = calcula_pedido(qtd, cardapio[cod][1])
        pedido_total = pedido_total + pedido
        print(f"{cardapio[cod][0]} - R${pedido}")
    conta = input("\nFechar conta? (s/n): ")

print(f"Valor da conta: R${pedido_total}")
#_#