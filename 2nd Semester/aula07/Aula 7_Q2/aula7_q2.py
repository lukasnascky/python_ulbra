from funcoes_q2 import *

qtd_notas = 0
total_notas = []

while True:
    nota = float(input("Nota: "))
    if nota < 0:
        break
    total_notas.append(nota)
    qtd_notas += 1

print(f"\nQuantidade de valores lidos: {qtd_notas}") ##letra a

print("\nNotas: ", total_notas, "\n") ##letra b

notas_contrario = total_notas[:] ##letra c
notas_contrario.reverse()
for i in notas_contrario:
    print(i)

print(f"\nSoma Notas: {soma_notas(total_notas)}") ##letra d

media = float(media_notas(total_notas, qtd_notas))
print(f"\nMédia: {media}") ##letra e

print(f"\nNotas acima da média: {notas_acima_media(total_notas, media)}") ##letra f

print(f"\nNotas abaixo de sete: {notas_abaixo_sete(total_notas)}") ##letra g

print("\nAté logo:)") ##letra h