from funcoes_q3 import *

valor_min = float(input("Valor mínimo: "))
total_indenizacao = 0
maior_valor_b = 0

metragem = float(input("Metragem: "))
while metragem != 0:
    classe = input("Classe(A/B): ")
    if classe == "A" and classe == "B":
        print("Classe inválida!")
    else:
        indenizacao = calcula_indenizacao(valor_min, metragem, classe)
        total_indenizacao = total_indenizacao + indenizacao
        if classe == "B" and indenizacao > maior_valor_b:
            maior_valor_b = indenizacao
        print(f"Indenização: R${indenizacao}")
    
    metragem = float(input("\nMetragem: "))

print(f"Total gasto com indenização: R${total_indenizacao}")
print(f"Maior valor pago em uma indenização classe B: R${maior_valor_b}")
#_#