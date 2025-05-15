from funcoes_q1 import *
lista = []

while True:
    palavra = input("Insira uma palavra:\n>>>")
    if palavra == "sair":
        break
    lista.append(palavra)

lista.sort(key=test)
print(lista)
#_#