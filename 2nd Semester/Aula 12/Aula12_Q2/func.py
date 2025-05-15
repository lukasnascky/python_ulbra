def cria_dicionario(palavras):
    dicionario = {}
    lista_palavras = palavras.lower().split(',')
    for palavra in lista_palavras:
        dicionario[palavra] = lista_palavras.count(palavra)
    return dicionario