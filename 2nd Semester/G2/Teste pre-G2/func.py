import json

def carregar_traducoes(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read().strip()
    traducoes = {}
    if conteudo:
        traducoes = json.loads(conteudo)
    arquivo.close()
    return traducoes

def salvar_traducao(nome_arquivo, traducoes):
    arquivo = open(nome_arquivo, 'w')
    traducoes_json = json.dumps(traducoes, indent=4)
    arquivo.write(traducoes_json)
    arquivo.close()
    return f"Tradução salva com sucesso!"

def traduz_ingles_portugues(nome_arquivo, frase):
    arquivo = open(nome_arquivo, 'r')
    traducoes = json.load(arquivo)
    frase_traduzida = ''
    for palavra in frase.split():
        if palavra in traducoes:
            frase_traduzida = frase_traduzida + ' ' + traducoes[palavra]
        else:
            frase_traduzida = frase_traduzida + ' ' + palavra 
    arquivo.close()
    return frase_traduzida

def traduz_portugues_ingles(nome_arquivo, frase):
    pass

def dicionario_ordem_alfabetica(nome_arquivo):
    pass

def lista_maiores_palavras(nome_arquivo):
    pass