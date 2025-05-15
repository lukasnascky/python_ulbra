def remove_primeiro_ultimo(lista):
    if len(lista) < 2:
        return []
    
    nova_lista = []
    nova_lista.extend(lista[1:-1])
    
    return lista[1:-1]
#_#