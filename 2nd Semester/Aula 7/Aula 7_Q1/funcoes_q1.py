def verifica_participacao(qtd_perguntas):
    if qtd_perguntas <= 1:
        return f"\nInocente!"

    elif qtd_perguntas == 2:
        return f"\nSuspeito!"

    elif qtd_perguntas <= 4:
        return f"\nCumplice!"

    else:
        return f"\nAssassino!"