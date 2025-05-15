#CRIA A LISTA DAS POLTRONAS
poltronas = [["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], 
             ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], 
             ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], 
             ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], 
             ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"], ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"]]
#VERIFICA SE AINDA HÁ VAGAS
ocupadas = 0
while ocupadas < 150:
    #MOSTRA AS POLTRONAS NA TELA
    i = 0
    while i < len(poltronas):
        if i < 10:
            print(i, " ", poltronas[i][0], poltronas[i][1], poltronas[i][2], poltronas[i][3], poltronas[i][4], 
                  poltronas[i][5], poltronas[i][6], poltronas[i][7], poltronas[i][8], poltronas[i][9])
        else:
            print(i, "", poltronas[i][0], poltronas[i][1], poltronas[i][2], poltronas[i][3], poltronas[i][4], 
                  poltronas[i][5], poltronas[i][6], poltronas[i][7], poltronas[i][8], poltronas[i][9])
        i = i + 1
    #COMPRA DE POLTRONA
    print("\nPoltronas ocupadas:", ocupadas)
    fileira = int(input("\nEscolha uma fileira: "))
    poltrona = int(input("Escolha uma poltrona: "))
    #VERIFICA SE A POLTRONA ESTÁ LIVRE
    if poltronas[fileira][poltrona] != "O":
        poltronas[fileira][poltrona] = "O"
        ocupadas = ocupadas + 1
        print("Compra realizada com sucesso!")
    else:
        print("Poltrona ocupada!")
    #ADCIONA UMA POLTRONA OCUPADA
print("Todas as poltronas foram ocupadas!")
#_#