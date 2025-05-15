from funcoes import *

alunos = []
notas = []
medias = []
qtd_alunos = 0

while True:
    aluno = input("\nAluno: ") #adciona aluno a lista alunos
    if aluno == "0":
        break
    alunos.append(aluno)
    qtd_alunos += 1

    nota = []
    for i in range(4): #adciona notas do aluno a lista notas
        nota.append(float(input("Nota: ")))
    notas.append(nota)

print("\nEscola Primavera - Gestão de Alunos\n" + "="*50)
for i in range(len(alunos)): #retorna lista alunos e notas
    print(f"{alunos[i]}: \t{notas[i]}")
print(f"\nForam processados {qtd_alunos} alunos!\n")

for i in range(len(alunos)): #retorna media e situação
    media = media_notas(notas, i)
    medias.append(media)
    print(f"{alunos[i]}\t|{media}\t|{situacao(media)}")

print("\n", "="*50)
print(f"Total de alunos aprovados: {calc_alunos_aprovados(medias)}")
print(f"Total de alunos reprovados: {calc_alunos_reprovados(medias)}")
print(f"A maior nota é do aluno {aluno_maior_nota(medias, alunos)} com valor {maior_nota(medias)}!")
print(f"A menor nota é do aluno {aluno_menor_nota(medias, alunos)} com valor {menor_nota(medias)}!")
print(f"Os dois primeiros alunos da lista são: {alunos[0]} e {alunos[1]}")
print(f"Os dois ultimos alunos da lista são: {alunos[-2]} e {alunos[-1]}")
print(f"Lista de alunos em ordem algabética: {lista_organizada(alunos)}")