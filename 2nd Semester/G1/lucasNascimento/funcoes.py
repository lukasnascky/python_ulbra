def media_notas(notas, posi):
    soma = notas[posi][0] + notas[posi][1] + notas[posi][2] + notas[posi][3]
    media = soma / 4
    return media

def situacao(media):
    if media >= 7:
        return f"Aprovado"
    return f"Reprovado"

def calc_alunos_aprovados(medias):
    aprovados = 0
    for i in medias:
        if i >= 7:
            aprovados += 1
    return aprovados

def calc_alunos_reprovados(medias):
    reprovados = 0
    for i in medias:
        if i < 7:
            reprovados += 1
    return reprovados

def aluno_maior_nota(medias, alunos):
    maior_nota = 0
    aluno_maior = ''
    for i in range(len(alunos)):
        if medias[i] > maior_nota:
            maior_nota = medias[i]
            aluno_maior = alunos[i]
    return aluno_maior

def maior_nota(medias):
    maior_nota = 0
    for i in range(len(medias)):
        if medias[i] > maior_nota:
            maior_nota = medias[i]
    return maior_nota

def aluno_menor_nota(medias, alunos):
    menor_nota = 99
    aluno_menor = ''
    for i in range(len(alunos)):
        if medias[i] < menor_nota:
            menor_nota = medias[i]
            aluno_menor = alunos[i]
    return aluno_menor

def menor_nota(medias):
    menor_nota = 99
    for i in range(len(medias)):
        if medias[i] < menor_nota:
            menor_nota = medias[i]
    return menor_nota

def lista_organizada(lista):
    lista.sort()
    return lista