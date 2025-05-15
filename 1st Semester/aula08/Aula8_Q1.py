sal_tot = 0
menor_sal = 9999999
menor_nome = ''
cont = 0

nome = input("Nome: ")
while nome != "fim":
    qtd_horas = float(input("Horas: "))
    valor_hora = float(input("Valor hora: "))
    sal = qtd_horas * valor_hora
    print("Salário:", sal)
    if sal < menor_sal:
        menor_sal = sal
        menor_nome = nome
    sal_tot = sal_tot + sal
    cont = cont + 1
    nome = input("\nNome: ")
print("\nMédia salarial:", sal_tot / cont)
print("Menor salário:", menor_sal, "\nNome(menor salário):", menor_nome)