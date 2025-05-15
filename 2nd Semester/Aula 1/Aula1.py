sair = input("Aperte qualquer tecla ou digite \"sair\" para finalizar")

while sair != "sair":
    aluno = input("Nome do Aluno: ")
    g1 = float(input("Nota 1: "))
    g2 = float(input("Nota 2: "))
    frequencia = int(input("Percentual de frequência: "))
    mp = (g1 + (g2 * 2)) / 3

    if mp >= 6 and frequencia >= 75: #se nota > 6 com frequencia
        print("\nAluno", aluno, "aprovado!\nNota:", mp)
    elif mp < 6 and frequencia >= 75: #se nota < 6 com frequencia
        print("\nAluno", aluno, "em recuperação!\nNota:", mp)
        ef = float(input("Nota Exame final: "))
        mf = (mp + (ef * 2)) / 3

        if mf < 6: #se nota final < 6
            print("\nAluno", aluno, "reprovado!\nNota:", mf)
        else: #se nota final > 6
            print("\nAluno", aluno, "aprovado!\nNota:", mf)
    else: #se não houver frequencia reprovação direta
        print("Aluno", aluno, "reprovado!\nNota:", mp)

    sair = input("\nAperte qualquer tecla ou digite \"sair\" para finalizar")