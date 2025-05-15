from funcoes_q3 import *

loja = []
ad_vendedor = ""

while ad_vendedor != "n":
    vendedor_vendas = []
    vendedor = input("\nVendedor: ")
    vendas = float(input("Quantidade vendida: "))

    tipo_comiss = verifica_comiss(vendas)

    vendedor_vendas.append(vendedor)
    vendedor_vendas.append(vendas)
    vendedor_vendas.append(tipo_comiss)
    loja.append(vendedor_vendas)

    ad_vendedor = input("\nAdcionar outro vendedor? s/n\n>>>")

for i in loja:
    print(f"Vendedor: {i[0]} | Vendas: R${i[1]} | Intervalo: {i[2]}")