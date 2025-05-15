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