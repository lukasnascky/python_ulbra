def maior_num_por_lista(lista):
    maiores_num = []

    for x in range(0, len(lista)):
        maior_num = 0
        for y in range(0, len(lista[x])):
            if y > maior_num:
                maior_num = y
        maiores_num.append(maior_num)

    return maiores_num
