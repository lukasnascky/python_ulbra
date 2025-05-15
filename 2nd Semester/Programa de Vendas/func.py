import json, os, datetime

def carregar_algo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read().strip()
    algo = {}
    if conteudo:
        algo = json.loads(conteudo)
    arquivo.close()
    return algo

def salvar_algo(nome_arquivo, algo):
    arquivo = open(nome_arquivo, 'w')
    vendas_json = json.dumps(algo, indent=4)
    arquivo.write(vendas_json)
    arquivo.close()

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def adciona_ao_carrinho(carrinho, item, valor_item, qtd_item, valor_a_pagar):
    carrinho[item] = {'valor_item': valor_item, 'qtd_item': qtd_item, 'valor_a_pagar': valor_a_pagar}
    salvar_algo('carrinho.json', carrinho)
    return carrinho

def remover_do_carrinho(carrinho, item_a_remover):
    if item_a_remover in carrinho:
        del carrinho[item_a_remover]
        salvar_algo('carrinho.json', carrinho)