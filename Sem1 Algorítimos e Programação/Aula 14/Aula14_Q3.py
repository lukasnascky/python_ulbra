i = 0
alunos = []
while i < 50:
    aluno = []
    aluno.append(input("Nome: "))
    aluno.append(float(input("Primeira nota: ")))
    aluno.append(float(input("Segunda nota: ")))
    media = (aluno[1] + aluno[2]) / 2
    print("Média:", media, "\n")
    aluno.append(media)
    alunos.append(aluno)
    i = i + 1
#TODAS AS NOTAS IMPRESSAS EM ORDEM
i = 0
while i < len(alunos):
    print(alunos[i])
    i = i + 1
#_#