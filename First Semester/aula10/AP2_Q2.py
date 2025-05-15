menor_veiculo = ''
menor_pass = 999999
mais_25_A = 0
pessoas_B = 0

veiculo = input("\nVeículo: ")
while veiculo != "X":
    data = input("Data: ")
    passageiros = int(input("Número de passageiros: "))
    valor_pass = float(input("Valor da passagem: "))
    despesas = float(input("Despesas totais: "))
    lucro = (passageiros * valor_pass) - despesas
    if lucro > 0:
        print("Teve lucro!")
    elif lucro < 0:
        print("Teve prejuízo!")
    else:
        print("Foi possível apenas pagar os gastos!")
    if veiculo == "A" and passageiros > 25:
        mais_25_A = mais_25_A + 1
    if veiculo == "B" and data == "10/10/23":
        pessoas_B = pessoas_B + passageiros
    if passageiros < menor_pass:
        menor_pass = passageiros
        menor_veiculo = veiculo
    veiculo = input("\nVeículo: ")

print("Excursões veículo A com mais da metade de passageiros:", mais_25_A)
print("Quantidade de pessoas que viajaram no veículo B no dia 10/10/23:", pessoas_B)
print("Veículo que transportou menos em uma viagem:", menor_veiculo)