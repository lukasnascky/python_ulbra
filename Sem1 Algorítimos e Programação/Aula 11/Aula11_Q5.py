media = []
cont = 0
while cont < 5:
    media.append(float(input("Média: ")))
    cont = cont + 1
#CALCULO DE MEDIA GERAL
cont = 0
total = 0
while cont < len(media):
    total = total + media[cont]
    cont = cont + 1
media_geral = total / 5
print("Média da turma:", media_geral)
#QUANTIDADE DE ALUNOS COM NOTA MAIOR QUE A MÉDIA GERAL
cont = 0
nota_acima = 0
while cont < len(media):
    if media[cont]> media_geral:
        nota_acima = nota_acima + 1
    cont = cont + 1
print(nota_acima, "alunos tiraram notas acima da média geral!")