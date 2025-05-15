from funcoes_rev1 import *

lista_func = []
lista_sal = []
qtd_func = 0

while True:
    func = input("Funcionário: ")
    if func == "0":
        break
    salario = float(input("Salário: "))

    lista_func.append(func)
    lista_sal.append(salario)
    qtd_func += 1

#Tabela de colaboradores e salarios
print("\nGESTÃO COLABORADORES HORIZON INOVATIONS\n" + "="*40)   #linhas 1 e 2
print("COLABORADOR \t\tSALÁRIO\n" + "="*40)                     #linhas 3 e 4
for i in range(len(lista_func)):                                #salarios
    print(f"{lista_func[i]}\t\t\tR${lista_sal[i]}")
print("="*40, f"\nTOTAL:\t\t\tR${total_salario(lista_sal)}")    #ultimas 2 linhas

#Outras saídas
print(f"\nForam processados {qtd_func} colaboradores!")
print(f"Número de trabalhadores com salário superior a 1412,00: {salario_superior(lista_sal)}")
print(f"Maior salário pago a {nome_maior_salario(lista_sal, lista_func)} com o valor de R${maior_salario(lista_sal)}")
print(f"Média dos salários pagos: R${media_salarios(lista_sal)}")
print(f"Os dois primeiros colaboradores da lista são: {lista_func[0]} e {lista_func[1]}")
print(f"Os dois ultimos colaboradores da lista são: {lista_func[-2]} e {lista_func[-1]}")
print(f"A lista salários organizada fica: {reorganiza_lista(lista_sal)}")
print(f"A lista de colaboradores em ordem alfabetica: {reorganiza_lista(lista_func)}")