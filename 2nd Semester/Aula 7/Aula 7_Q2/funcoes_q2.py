def soma_notas(lista_notas):
    soma = 0
    for i in lista_notas:
        soma += i
    return soma

def media_notas(lista_notas, qtd_notas):
    soma = 0
    for i in lista_notas:
        soma += i
    
    media = soma / qtd_notas
    return "{:.2f}".format(media)

def notas_acima_media(lista_notas, media):
    notas_acima = 0
    for i in lista_notas:
        i_float = float(i)
        if i_float > media:
            notas_acima += 1
    return notas_acima

def notas_abaixo_sete(lista_notas):
    notas_abaixo = 0
    for i in lista_notas:
        if i < 7:
            notas_abaixo += 1
    return notas_abaixo