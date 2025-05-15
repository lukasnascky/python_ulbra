def separa_pares_impares(lista):
    lista_pares = []
    lista_impares = []
    for x in range(0, len(lista)):
        if lista[x] % 2 == 0:
            lista_pares.append(lista[x])
        else:
            lista_impares.append(lista[x])
    return f"Pares: {lista_pares}\nImpares: {lista_impares}"
#_#