jogadores = [["Alice", "Feminino", 4.0, 4.0, 3.5],
        ["Beto", "Masculino", 4.0, 3.5, 3.0],
        ["Carla", "Feminino", 2.0, 2.5, 2.0],
        ["Davi", "Masculino", 4.0, 4.0, 3.5],
        ["Eva", "Feminino", 2.5, 2.0, 3.5]]
#INSERIR DADOS DE UM NOVO JOGADOR
continuar = input("\nDeseja adcionar um jogador? s/n: ")
while continuar == "s":
    jogador = []
    jogador.append(input("Digite o nome do jogador: "))
    jogador.append(input("Digite a categoria do jogador: "))
    jogador.append(int(input("Digite a pontuação do primeiro torneio: ")))
    jogador.append(int(input("Digite a pontuação do segundo torneio: ")))
    jogador.append(int(input("Digite a pontuação do terceiro torneio: ")))
    jogadores.append(jogador)
    continuar = input("\nDeseja adcionar outro jogador? s/n: ")
print(jogadores)
#PONTUAÇÃO MEDIA DOS TRÊS TORNEIOS PARA CADA JOGADOR
i = 0
pont_media = []
while i < len(jogadores):
    soma = jogadores[i][2] + jogadores[i][3] + jogadores[i][4]
    media = soma / 3
    jogadores[i].append(media)
    i = i + 1
print("\n", jogadores)
#SOLICITA AO USUARIO UM NOME E APRESENTA A CATEGORIA E A PONTUAÇÃO MEDIA
encontrar = input("\nNome do jogador: ")
i = 0
cod_encontrar = 0
while i < len(jogadores):
    if encontrar == jogadores[i]:
        cod_encontrar = i
    i = i + 1
print("Categoria:", jogadores[cod_encontrar][1])
print("Pontuação média:", jogadores[cod_encontrar][5])
#ALTERAR USUARIO
indice = int(input("\nLinha desejada para alteração: "))
if indice <= len(jogadores) and indice >= 0:
    novo_nome = input("Digite o novo nome: ")
    jogadores[indice][0] = novo_nome
    print("Nome alterado com sucesso!\n", jogadores)
else:
    print("Não foi possível localizar a linha selecionada!")
#_#