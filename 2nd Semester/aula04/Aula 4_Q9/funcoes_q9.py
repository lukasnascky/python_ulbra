def remove_primeiros_ultimos(lista):
    tam_ = len(lista)

    meio1 = tam_ // 2 - 1
    meio2 = tam_ // 2 + 1

    nova_lista = lista[meio1:meio2]

    return nova_lista
#_#