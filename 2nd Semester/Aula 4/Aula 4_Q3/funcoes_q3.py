def alterna_lista(lista1, lista2):
    lista3 = []
    tamanho_min = min(len(lista1), len(lista2))

    for x in range(tamanho_min):
        lista3.append(lista1[x])
        lista3.append(lista2[x])
    
    lista3.extend(lista1[tamanho_min:])
    lista3.extend(lista2[tamanho_min:])

    return lista3
#_#