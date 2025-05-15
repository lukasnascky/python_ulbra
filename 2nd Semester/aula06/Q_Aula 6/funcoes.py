#count
def l_count(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador = contador + 1
    return contador

#extend
def l_extend(lista1, lista2):
    for i in lista1:
        lista2.append(i)
    return lista2

#insert
def l_insert(lista, posi, item):
    lista2 = []
    for i in range(posi):
        lista2.append(lista[i])
    lista2.append(item)
    for i in range(posi, len(lista)):
        lista2.append(lista[i])
    return lista2

#remove
def l_remove(lista, item):
    lista2 = []
    for i in lista:
        if i == item:
            pass
        else:
            lista2.append(i)
    return lista2

#pop
def l_pop(lista, posi):
    lista2 = []
    for i in lista:
        if i == lista[posi]:
            pass
        else:
            lista2.append(i)
    return lista2

#index
def l_index(lista, item):
    count = 0
    count_itens = []
    for i in lista:
        if i == item:
            count_itens.append(count)
        count += 1
    return count_itens

#sort
def l_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#reverse
def l_reverse(lista):
    return lista[::-1]