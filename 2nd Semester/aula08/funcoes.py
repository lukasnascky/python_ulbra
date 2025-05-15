def calcula_abono(salarios):
    abonos = []
    for i in salarios:
        if i > 500:
            abono = i * 0.2
        else:
            abono = 100
        abonos.append(abono)
    return abonos

def soma_salarios(salarios):
    soma = 0
    for i in salarios:
        soma += i
    return soma

def soma_abonos(abonos):
    soma = 0
    for i in abonos:
        soma += i
    return soma

def abonos_min(abonos):
    abono_min = 0
    for i in abonos:
        if i == 100:
            abono_min += 1
    return abono_min

def maior_abono(abonos):
    maior_abono_ = 0
    for i in abonos:
        if i > maior_abono_:
            maior_abono_ = i
    return maior_abono_

def colaborador_maior_abono(colaboradores, abonos):
    colab_maior_abono = ""
    maior_abono = 0
    for i in range(len(abonos)):
        if abonos[i] > maior_abono:
            colab_maior_abono = colaboradores[i]
            maior_abono = abonos[i]
    return colab_maior_abono

def media_abono(abonos, qtd_colaboradores):
    soma = 0
    for i in abonos:
        soma += i
    media = soma / qtd_colaboradores
    return media

def abonos_acima_media(abonos, media):
    qtd_acima = 0
    for i in abonos:
        if i > media:
            qtd_acima += 1
    return qtd_acima