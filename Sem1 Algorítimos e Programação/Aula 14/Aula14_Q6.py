i = 0
pontos = 0
lista = [["vermelho", "red"], ["azul", "blue"], ["amarelo", "yellow"], ["laranja", "orange"], ["preto", "black"], 
         ["branco", "white"], ["cinza", "gray"], ["rosa", "pink"], ["ciano", "cyan"], ["marrom", "brown"], 
         ["lima", "lime"], ["verde", "green"], ["roxo", "purple"], ["bege", "beige"], ["vinho", "burgundy"], 
         ["mostarda", "mustard"], ["salmão", "salmon"], ["violeta", "violet"], ["caramelo", "caramel"], ["lilás", "lilac"]]
respostas = []
while i < 5:
    i2 = 0
    ja_foi = 0
    #SOLICITA UMA LINHA E VERIFICA SE JA FOI DIGITADA ANTERIORMENTE
    linha = int(input("\nLinha: "))
    while i2 < len(respostas):
        if linha == respostas[i2]:
            ja_foi = ja_foi + 1
        i2 = i2 + 1
    if ja_foi < 1:
        print("Português:", lista[linha][0])
        #SOLICITA RESPOSTA
        resposta = input("Inglês: ")
        #VERIFICAÇÃO DE RESPOSTA CORRETA
        if resposta == lista[linha][1]:
            print("Resposta correta!\n", "+1 ponto!")
            pontos = pontos + 1
        else:
            print("Resposta incorreta!\n", "0 pontos!")
    else:
        print("Essa linha já foi selecionada anteriormente!\n0 pontos!")
    respostas.append(linha)
    i = i + 1
#PONTUAÇÃO TOTAL
print("\nPontuação:", pontos, "pts")
#_#