def verifica_aparicoes(lista):
    for x in range(len(lista)):
        if lista.count(x) > 1:
            return True   
    return False
#_#