from funcoes import *

while True: 
    menu = int(input('''
1. Soma CPF (nnn + nnn + nnn + nn)
2. Verifica palavra
3. Ultimas duas palavras
4. Ultima palavra
5. Todas menos as duas últimas
6. Todas menos a ultima
7. Iniciais ponto e espaço
8. Verifica preposição
9. Junção da 7 e da 8
10. Frase em maiúscula
11. Frases concatenadas
0. Sair
>>>'''))
    if menu == 0: #finaliza o programa
        break
    
    elif menu == 1: #soma todos os digitos do cpf
        cpf = input("\nCPF(nnn.nnn.nnn-nn): ")
        print(soma_cpf(cpf))
    
    elif menu == 2: #retorna True para 'Junior', 'Filho', 'Neto' ou 'Sobrinho'
        palavra = input("\nPalavra: ")
        print(ver_palavras_especificas(palavra))

    elif menu == 3: #retorna as duas ultimas palavras da frase
        frase = input("\nFrase: ")
        print(duas_ultimas_palavras(frase))
    
    elif menu == 4: #retorna a ultima palavra da frase
        frase = input("\nFrase: " )
        print(ultima_palavra(frase))
    
    elif menu == 5: #retorna a frase menos as duas ultimas
        frase = input("\nFrase: " )
        print(palavras_menos_ultimas(frase))

    elif menu == 6: #retorna a frase menos a ultima
        frase = input("\nFrase: " )
        print(palavras_menos_ultima(frase))
    
    elif menu == 7: #separa palavras e retorna as iniciais com ponto e espaço
        lista = []
        print(" ")
        while True:
            palavra = input("Palavra ('0' para sair): ")
            if palavra == "0":
                break
            lista.append(palavra)
        print(iniciais_ponto_espaco(lista))
    
    elif menu == 8: #retorna True se esta palavra for 'da', 'de', 'das', 'do', 'dos' ou 'e'
        palavra = input("\nPalavra: ")
        print(ver_preposicao_especifica(palavra))
    
    elif menu == 9: #junção da 7 e da 8
        lista = []
        print(" ")
        while True:
            palavra = input("Palavra ('0' para sair): ")
            if palavra == "0":
                break
            lista.append(palavra)
        print(iniciais_ponto_espaco_preposicao(lista))
    
    elif menu == 10: #retorna frase em maiúscula
        frase = input("\nFrase: ")
        print(frase.upper())
    
    elif menu == 11: #retorna frases concatenadas
        frase = input("\nFrase: ")
        frase2 = input("Frase 2: ")
        print(concatena_frases(frase, frase2))