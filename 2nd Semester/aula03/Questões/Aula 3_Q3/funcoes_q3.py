def calcula_indenizacao(valor_min, metros, classe):
    if classe == "A":
        indenizacao = valor_min + (500 * metros)
    elif classe == "B":
        indenizacao = valor_min + (300 * metros)
    return indenizacao
#_#