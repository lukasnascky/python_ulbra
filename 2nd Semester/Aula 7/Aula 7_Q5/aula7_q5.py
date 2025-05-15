from funcoes_q5 import *

jogadores = [0]*23
num_jogadores = []
qtd_votos = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    num_jogador = int(input("Número:"))
    if num_jogador == 0:
        break
    elif num_jogador < 0 or num_jogador > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
    else:
        jogadores[num_jogador - 1] += 1
        qtd_votos += 1

    for i in jogadores:
        if i > 0:
            num_jogadores.append(jogadores[i+1])
    num_jogadores.sort()
    num_jogadores.reverse()

    

print(f"Foram computados {qtd_votos} votos!")
print(jogadores)