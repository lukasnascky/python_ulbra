def ordenada_desordenada_tf(lista):
    
    for x in range(1, len(lista)):
        if lista[x] < lista[x - 1]:
            return False
    return True
#_#