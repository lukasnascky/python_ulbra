from funcoes_q4 import *

menu = int(input("[1]Pode votar?\n[2]Ver Categoria\n[3]Pode alistar\n[4]Encerrar programa\n>>>"))

while menu != 4:
    if menu == 1: #Verfifica se pode votar
        idade = int(input("\nIdade: "))
        nacionalidade = input("Nacionalidade: ")
        print(verifica_pode_votar(idade, nacionalidade))

    elif menu == 2: #Informa categoria do usuário
        idade = int(input("\nIdade: "))
        print(verifica_categoria(idade))

    elif menu == 3: #Verifica se pode se alistar
        idade = int(input("\nIdade: "))
        sexo = input("Sexo(m/f): ")
        print(verifica_alistamento(idade, sexo))
    
    menu = int(input("\n[1]Pode votar?\n[2]Ver Categoria\n[3]Pode alistar\n[4]Encerrar programa\n>>>"))
#_#