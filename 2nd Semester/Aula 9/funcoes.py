def soma_cpf(cpf):
    soma = 0
    lista1 = cpf.split("-")
    lista2 = lista1[0].split(".")
    lista2.extend(lista1[1])
    for i in lista2:
        soma += int(i)
    return soma

def ver_palavras_especificas(palavra):
    if palavra == "Junior" or palavra == "Filho" or palavra == "Neto" or palavra == "Sobrinho":
        return True
    return False

def  duas_ultimas_palavras(frase):   
    palavras = frase.split()
    duas_ultimas = ' '.join(palavras[-2:])
    return duas_ultimas

def ultima_palavra(frase):
    palavras = frase.split()
    return palavras[-1]

def palavras_menos_ultimas(frase):
    palavras = frase.split()
    return palavras[:-2]

def palavras_menos_ultima(frase):
    palavras = frase.split()
    return palavras[:-1]

def iniciais_ponto_espaco(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.extend(lista[i][0])
    lista2.append(' ')
    letras = '. '.join(lista2[:])
    return letras

def ver_preposicao_especifica(palavra):
    compara = ['da', 'de', 'das', 'do', 'dos', 'e']
    for i in compara:
        if palavra == i:
            return True
    return False

def iniciais_ponto_espaco_preposicao(lista):
    lista2 = []
    compara = ['da', 'de', 'das', 'do', 'dos', 'e']
    for i in range(len(lista)):
        if lista[i] in compara:
            lista2.append(lista[i])
        else:
            lista2.append(lista[i][0])
    lista2.append(' ')
    letras = '. '.join(lista2)
    return letras

def concatena_frases(frase, frase2):
    frase_conc = frase + ", " + frase2
    return frase_conc