listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
#VALIDA O MÊS ESCOLHIDO
mes = int(input("Digite o mês: "))
while mes < 1 and mes > 12:
    mes = input("\nDigite um mês válido: ")
#MOSTRA A DATA DE ANIVERSÁRIO COM O MêS POR EXTENSO
print("Você nasceu no mês de", listaMeses[mes - 1])
#_#