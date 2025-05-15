cont = 0
lucro = 0
lucrotot = 0

while cont < 5:
    pcocompra = float(input("Preço de compra: "))
    pcovenda = float(input("Preço de venda: "))
    lucro = pcovenda - pcocompra
    print("Lucro:", lucro, "\n")
    lucrotot = lucrotot + lucro
    cont = cont + 1
print("Média de lucro:", lucrotot / cont)