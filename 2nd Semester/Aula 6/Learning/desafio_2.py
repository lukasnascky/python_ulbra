def soma_numeros(*johnSennapaparapan):
    soma = 0
    for numero in johnSennapaparapan:
        soma = soma + numero
    return soma

print(soma_numeros(1, 1, 9, 8, 5))

pessoas = (("Joao", 20),("Maria", 25),("James", 20))

for nome, idade in pessoas:
    print(f"Nome: {nome} | Idade: {idade}")