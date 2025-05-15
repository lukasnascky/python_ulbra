def calculo_media(nota1, nota2):
    media1 = (nota1 + (nota2 * 2))/3
    return media1

while True:
    nomeAluno = input('Entre com o nome do aluno ou digite "sair" para encerrrar: ')
    if nomeAluno == 'sair':
        break
    notaG1 = float(input("Nota G1: "))
    notaG2 = float(input("Nota G2: "))
    frequencia = int(input("Entre com a frequência: "))
    mp = calculo_media(notaG1, notaG2)
    
    if frequencia < 75:
        print(f"O aluno {nomeAluno} foi reprovado por falta.")
    elif mp >= 6:
        print(f"O aluno {nomeAluno} foi aprovado.")
    else:
        ef = float(input("Entre com a nota de EF: "))
        mf = calculo_media(mp, ef)
        if mf >= 6:
            print(f"O aluno {nomeAluno} foi aprovado.")
        else:
            print(f"O aluno {nomeAluno} foi reprovado.")