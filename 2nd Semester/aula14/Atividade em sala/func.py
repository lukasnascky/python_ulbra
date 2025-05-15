import json

def carregar_produtos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read().strip()
    produtos = {}
    if conteudo:
        produtos = json.loads(conteudo)
    arquivo.close()
    return produtos

def salvar_produto(nome_arquivo, produtos):
    arquivo = open(nome_arquivo, 'w')
    produtos_json = json.dumps(produtos, indent=4)
    arquivo.write(produtos_json)
    arquivo.close()
    return f"Livro cadastrado com sucesso!"

def lista_livros(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    produtos = json.load(arquivo)
    for produto, detalhes in produtos.items():
        print(f"{produto} - {detalhes['titulo']} - {detalhes['quantidade']}")
    arquivo.close()

def excluir_livro(nome_arquivo, livro):
    pass
    #arquivo = open(nome_arquivo, 'w')
    #produtos = json.dumps(arquivo)
    
    #arquivo.close()
    #return "Livro excluido com sucesso!"

def pesquisa_livro(nome_arquivo, livro):
    arquivo = open(nome_arquivo, 'r')
    produtos = json.load(arquivo)
    if livro in produtos:
        return f"{livro} - {livro['nome']}"
    else:
        for produto, detalhes in produtos.items():
            print(f"{produto} - {detalhes['titulo']} - {detalhes['quantidade']}")


def relatorio_livros(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    produtos = json.load(arquivo)
    for produto, detalhes in produtos.items():
        if int(detalhes['quantidade']) == 0:
            print(f"{produto} - {detalhes['titulo']}")
    arquivo.close()