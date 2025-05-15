import random

def gera_aleatorios(cont):
    lista = []
    for x in range(cont):
        lista.append(random.randint(1, cont))

    return lista
    #_#