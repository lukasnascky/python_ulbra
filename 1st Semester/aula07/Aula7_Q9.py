cont = 0
sal_min = float(input("Salário mínimo: "))
maior_sal = 0
setor_r = 0
per_setor = 0

while cont < 30:
    nome = input("\nNome: ")
    setor = input("Setor (r - roupas ou c - calçados): ")
    vendas = float(input("Quantia vendida: "))
    sal_tot = sal_min + ((8 / 100) * vendas)
    print("Salário mensal: ", sal_tot)
    if setor == "r":
        setor_r = setor_r + 1
    if sal_tot > maior_sal:
        maior_sal = sal_tot
    cont = cont + 1
if setor_r > 0:
    per_setor = (setor_r / 3) * 100
print("\nPercentual de vendedores do setor de roupas:", per_setor, "%")
print("Maior Salário:", maior_sal)