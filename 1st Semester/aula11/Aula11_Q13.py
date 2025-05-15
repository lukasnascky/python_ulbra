G = []
R = []
i = 0
#GABARITO
while i < 10:
    G.append(input("Gabarito: "))
    i = i + 1
#RESPOSTAS DO ALUNO
i = 0
while i < 10:
    R.append(input("Respostas: "))
    i = i + 1
#CONTABILIZAR OS ERROS
erros = []
acertos = []
i = 0
while i < 10:
    if G[i] != R[i]:
        erros.append(i)
    else:
        acertos.append(i)
    i = i + 1
#QUANTIDADE DE ACERTOS
i = 0
while i < len(erros):
    print("Erros: ", erros[i])
    i = i + 1
if acertos > 6:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")