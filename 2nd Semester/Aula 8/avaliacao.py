from funcoes import *

colaboradores = []
salarios = []
qtd_colaboradores = 0

print("\tPROJEÇÃO DE GASTOS COM ABONO")
print("="*50)

while True: 
    colaborador = input("\nColaborador: ") 
    if colaborador == "0":
        break
    salario = float(input("Salário: "))

    colaboradores.append(colaborador)
    salarios.append(salario)
    qtd_colaboradores += 1

abonos = calcula_abono(salarios)
media_abonos = media_abono(abonos, qtd_colaboradores)

print("\nCOLAB\t\t SALÁRIO\t  ABONO")
print("="*50)
for i in range(len(colaboradores)):
    print(colaboradores[i], "\t\tR$", salarios[i], "\tR$", abonos[i])
print("="*50)
print("TOTAL:", "\t\tR$", soma_salarios(salarios), "\tR$", soma_abonos(abonos))
print(f"\nForam processados {qtd_colaboradores} colaborador(es)!")
print(f"Total gasto com salários e abonos: R${soma_salarios(salarios) + soma_abonos(abonos)}")
print(f"Valor mínimo pago a {abonos_min(abonos)} colaborador(es)!")
print(f"Maior abono pago a {colaborador_maior_abono(colaboradores, abonos)}: R$ {maior_abono(abonos)}")
print(f"Média de abono pago: R$ {media_abonos}")
print(f"Foram pagos abono acima da média a {abonos_acima_media(abonos, media_abonos)} colaborador(es)!")