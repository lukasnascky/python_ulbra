import random
numeros = []
i = 0
while i < 10:
    numeros.append(random.randint(10, 15))
    i = i + 1
print("Numeros:", numeros)
#MENU DE ESCOLHAS
menu = int(input("\nSelecione a opção desejada:\n[1]Imprime tudo\n[2]Imprime número\n[3]Imprime posições\n[4]Altera\n[5]Encerrar\n>"))
while menu >= 1 and menu <= 4:
    if menu == 1:
        print("\n", numeros)
    elif menu == 2:
        posicao = int(input("\nDigite a posição desejada: "))
        if posicao < len(numeros) and posicao > 0:
            print(numeros[posicao])
        else:
            print("Erro! Posição inválida!")
    elif menu == 3:
        num = int(input("\n Digite um número que deseja localizar: "))
        i = 0
        if num in numeros:
            while i < len(numeros):
                if numeros[i] == num:
                    print("Posição:", i)
                i = i + 1
        else:
            print("O número não está na lista!")
    elif menu == 4:
        posicao = int(input("\nDigite a posição desejada: "))
        if posicao < len(numeros) and posicao > 0:
            novo_valor = int(input("Digite um novo valor: "))
            numeros[posicao] = novo_valor
            print(numeros)
        else:
            print("Posição inválida!")
    menu = int(input("\nSelecione a opção desejada:\n[1]Imprime tudo\n[2]Imprime número\n[3]Imprime posições\n[4]Altera\n[5]Encerrar\n>"))
print("Programa encerrado!")