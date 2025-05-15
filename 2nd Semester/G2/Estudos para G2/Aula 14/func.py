import json 

def carregar_livros(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read().strip()
    livros = {}
    if conteudo:
        livros = json.loads(conteudo)
    arquivo.close()
    return livros

def salvar_livros(nome_arquivo, livros):
    arquivo = open(nome_arquivo, 'w')
    livros_json = json.dumps(livros, indent=4)
    arquivo.write(livros_json)
    arquivo.close()

def listar_livros(livros):
    for livro, info in livros.items():
        print(f"{livro} - {info['titulo']} - {info['qtd']}")

def deletar_livro(livros, livro_a_deletar):
    if livro_a_deletar in livros:
        del livros[livro_a_deletar]
    else:
        return f"O livro solicitado não existe!"
    return livros

def pesquisar_livro(livro_a_pesquisar, livros):
    titulo_livro = livro_a_pesquisar.split()
    for livro, info in livros.items():
        for palavra in titulo_livro:
            if palavra in info['titulo'].split():
                print(f"\nISBN: {livro}\nTítulo: {info['titulo']}\nAutor: {info['autor']}\n Gênero: {info['genero']}\nPreço de Compra: {info['preco_compra']}\nPreço de Venda: {info['preco_venda']}\nQuantidade: {info['qtd']}")
            else:
                return f"Título não encontrado!"

def listar_livros_sem_estoque(livros):
    for livro, info in livros.items():
        if info['qtd'] == '0':
            print(f"{livro} - {info['titulo']}")