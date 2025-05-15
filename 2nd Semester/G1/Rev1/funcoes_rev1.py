def total_salario(lista_sal):
    soma_sal = 0
    for i in lista_sal:
        soma_sal += i
    return soma_sal

def salario_superior(lista_sal):
    qtd_sal_maior = 0
    for i in lista_sal:
        if i > 1412:
            qtd_sal_maior += 1
    return qtd_sal_maior

def maior_salario(lista_sal):
    maior_sal = 0
    for i in lista_sal:
        if i > maior_sal:
            maior_sal = i
    return maior_sal

def nome_maior_salario(lista_sal, lista_func):
    maior_sal = 0
    for i in range(len(lista_sal)):
        if lista_sal[i] > maior_sal:
            maior_sal = lista_sal[i]
            nome_maior_sal = lista_func[i]
    return nome_maior_sal

def media_salarios(lista_sal):
    soma = 0
    for i in lista_sal:
        soma += i
    media = soma / len(lista_sal)
    return media

def reorganiza_lista(lista):
    lista.sort()
    return lista