from funcoes_q5 import *

pgto_vendedores = 0
menor_qtd_camisetas = 9**99

salario_min = float(input("Salário mínimo: ")) 
nome = input("Nome do vendedor: ")

while nome != "sair":
    qtd_camisetas = int(input("Quantidade de camisetas vendidas: "))
    valor_recebido = salario_min + (qtd_camisetas * 0.5)
    print(verifica_categoria(nome, salario_min, qtd_camisetas))

    if qtd_camisetas < menor_qtd_camisetas: 
        menor_qtd_camisetas = qtd_camisetas
        vendr_menos_vendeu = nome

    pgto_vendedores = pgto_vendedores + valor_recebido

    nome = input("Nome do vendedor: ")

print(f"\nPagamento total: R${pgto_vendedores}\nVendedor que menos vendeu: {vendr_menos_vendeu}")