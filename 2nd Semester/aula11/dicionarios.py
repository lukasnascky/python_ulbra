pessoas = {}

cont = 1

while True:
    dados = input("nome,idade (0 para sair):")
    if dados == '0':
        break
    nome, idade = dados.split(",")
    pessoas[cont] = {"nome": nome, "idade": idade}
    cont += 1

for chave, pessoa in pessoas.items():
    print(f"")