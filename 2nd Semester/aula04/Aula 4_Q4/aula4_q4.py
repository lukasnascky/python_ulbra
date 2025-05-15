from funcoes_q4 import *

lista = []

while True:
    palavra = input("Insira um parâmetro:\n>>>")
    if palavra == "sair":
        break
    lista.append(palavra)

print("\n",retorna_pos_par(lista))
#_#