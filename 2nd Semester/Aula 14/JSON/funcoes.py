import json

def salvar_produtos(nome_arquivo, produtos):
    arquivo = open(nome_arquivo, 'w')
    produtos_json = json.dumps(produtos, indent=4)
    arquivo.write(produtos_json)
    arquivo.close()

def carregar_produtos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read()
    produtos = json.loads(conteudo)
    arquivo.close()
    return produtos


#    arquivo = open(nome_arquivo, "w")
#    for codigo, produto in produtos.items():
#        arquivo.write(f"{codigo},{produto['nome']}\n")
#    arquivo.close()