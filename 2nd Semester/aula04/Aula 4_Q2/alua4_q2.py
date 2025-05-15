from funcoes_q2 import *
lista = []

while True:
    palavra = input("Insira uma palavra:\n>>>")
    if palavra == "sair":
        break
    lista.append(palavra)

organiza_palavras(lista)
print(lista)
#_#