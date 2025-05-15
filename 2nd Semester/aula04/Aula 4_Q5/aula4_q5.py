from funcoes_q5 import *

lista = []

while True:
    palavra = input("Insira uma palavra:\n>>>")
    if palavra == "sair":
        break
    lista.append(palavra)

print("\nlista: ", lista, "\nlista ordenada:", ordena_alfabetica(lista))
#_#