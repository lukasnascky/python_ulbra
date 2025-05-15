def media_saltos(lista_saltos):
    soma = 0
    for i in lista_saltos:
        soma += i
    media = soma / 5

    return "{:.2f}".format(media) 