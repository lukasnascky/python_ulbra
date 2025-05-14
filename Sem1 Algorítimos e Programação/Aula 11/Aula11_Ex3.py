nome = []
cont = 0
while cont < 4:
    nome.append(input("Nome: "))
    cont = cont + 1
print("Tamanho:", len(nome), nome)
nome[0] = input("Nome: ")
print("Tamanho:", len(nome), nome)