from funcoes import *

frase = input("Frase: ") #1.a) Retorna as menores palavras
print(f"Menor palavra na frase: {menor_palavra(frase)}") 

print(f"Frase corrigida: {corrige_m_n(frase)}") #1.b) Corrige M e N antes de P e B

menu = input("\nPalavra (0 para sair): ") #2. Apresenta quantidade de ocorrências das palavras na frase
lista = []
while menu != "0":
    lista.append(menu)
    menu = input("Palavra (0 == sair): ")
ocorrencias = contar_objetos(lista)
total = 0
print("\nQuantidade de objetos cadastrados na lista: ")
for i in ocorrencias:
    print(f"\t{i[0]} - {i[1]}")
    total += i[1]
print(f"Total de objetos: {total}")

palavra = input("\nPalavra: ") #3. Verifica se a palavra digitada é um palíndromo
print(verifica_palindromo(palavra))

frase = input("\nFrase: ") #4. Retorna o percentual de vogais na frase
print(f"Percentual de vogais: {percentual_vogais(frase)}%")

frase = input("\nFrase para codificar: ") #5.a) Codifica mensagem
print(codificar_frase(frase))

frase = input("\nFrase pra decodificar: ") #5.a) Descodifica mensagem
print(decodificar_frase(frase))