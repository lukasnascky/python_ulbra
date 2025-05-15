pessoas = [['Ana Maria', 10], ['Pedro', 20], ['Carlos', 8], ['Carla', 18]]
#ADCIONA PESSOA A LISTA
continuar = input("Deseja adcionar um nome? s/n: ")
while continuar == 's':
    pessoa = []
    pessoa.append(input("Nome: "))
    pessoa.append(int(input("Idade: ")))
    pessoas.append(pessoa)
    continuar = input("\nDeseja adcionar outro nome? s/n: ")
print(" ")
#LISTA COM NOME E IDADE DO LADO
i = 0
while i < len(pessoas):
    print("Nome: ", pessoas[i][0], "| Idade:", pessoas[i][1], "anos")
    i = i + 1
print(" ")
#MAIOR OU MENOR DE IDADE???
i = 0
while i < len(pessoas):
    if pessoas[i][1] < 18:
        print("Nome: ", pessoas[i][0], "é menor de idade!")
    else:
        print("Nome: ", pessoas[i][0], "é maior de idade!")
    i = i + 1
#ENCONTRAR UMA PESSOA
encontrar = input("\nDigite o nome da pessoa que deseja encontrar: ")
i = 0
while i < len(pessoas):
    if encontrar == pessoas[i][0]:
        print("Idade:", pessoas[i][1], "anos")
    elif i == len(pessoas) - 1:
        print("Pessoa não encontrada!")
    i = i + 1