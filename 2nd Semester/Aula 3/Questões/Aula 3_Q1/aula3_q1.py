from funcoes_q1 import *

viagens_onibus_a = 0
qtd_pass_onibus_b = 0
onibus_mais_pass = 0

print("-" * 60)
id_onibus = input("Identificação do onibus: ")

while id_onibus != "X":
    data = input("Data: ")
    qtd_passageiros = int(input("Quantidade de passagerios: "))
    valor_passagem = float(input("Valor da passagem: "))
    despesas = float(input("Despesas da viagem: "))

    #a. Onibus, data e mensagem de lucro
    print("-" * 60)
    print(f"Onibus: {id_onibus}\nData: {data}\n{verifica_lucro(despesas, qtd_passageiros, valor_passagem)}")

    #b. Qtd viagens feitas pelo onibus A
    if id_onibus == "A":
        viagens_onibus_a = viagens_onibus_a + 1
    
    #c. Qtd de pessoas q viajou no onibus B no dia 23/12/22
    if id_onibus == "B" and data == "231222":
        qtd_pass_onibus_b = qtd_pass_onibus_b + qtd_passageiros

    #d. onibus que mais transportou passageiros em uma viagem
    if qtd_passageiros > onibus_mais_pass:
        onibus_mais_pass = qtd_passageiros
        id_onibus_mais_pass = id_onibus
        
    print("-" * 60)
    id_onibus = input("Identificação do onibus: ") #flag

print("-" * 60)
print(f"{viagens_onibus_a} viagens foram feitas pelo onibus 'A'.")
print(f"{qtd_pass_onibus_b} pessoas viajaram no onibus 'B' no dia 23/12/22.")
print(f"{id_onibus_mais_pass} foi o onibus com a mais passageiros em uma viagem:\n{onibus_mais_pass} passageiros.")
print("-" * 60)
#_#