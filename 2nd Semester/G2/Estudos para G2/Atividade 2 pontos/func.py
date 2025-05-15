import json

def carregar_dicionario(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read().strip()
    dicionario = {}
    if conteudo:
        dicionario = json.loads(conteudo)
    arquivo.close()
    return dicionario

def salvar_dicionario(nome_arquivo, dicionario):
    arquivo = open(nome_arquivo, 'w')
    dicionario_json = json.dumps(dicionario, indent=4)
    arquivo.write(dicionario_json)
    arquivo.close()

def traduzir_ingles_portugues(frase_ingles, dicionario):
    frase_traduzida = ''
    for palavra in frase_ingles:
        if palavra in dicionario:
            frase_traduzida = frase_traduzida + ' ' + dicionario[palavra]
        else:
            frase_traduzida = frase_traduzida + ' ' + palavra
    return frase_traduzida
