from funcoes_q1 import *

qtd_perguntas = 0
perguntas = ["1. Telefonou para a vítima? s/n", "2. Esteve no local do crime? s/n", "3. Mora perto da vítima? s/n", "Devia para a vítima? s/n", "Já trabalhou com a vítima? s/n"]

for i in range(len(perguntas)):
    print(perguntas[i])
    respota = input(">>>")
    if respota == "s":
        qtd_perguntas += 1

print(verifica_participacao(qtd_perguntas))