def retorna_pos_par(lista):
    lista_pares = []
    for x in range(0, len(lista)):
        if x % 2 == 0:
            lista_pares.append(lista[x])
    return lista_pares
#_#