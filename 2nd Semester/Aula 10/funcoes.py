def menor_palavra(frase):
    palavras = frase.split()
    palavra_menor = []
    tam_palavra_menor = 999999999
    for i in palavras:
        if len(i) <= tam_palavra_menor:
            palavra_menor.append(i)
            tam_palavra_menor = len(i)
    return palavra_menor

def corrige_m_n(frase):
    frase = frase.replace("nb", "mb").replace("np", "mp")
    return frase

def contar_objetos(lista):
    ocorrencias = []
    for i in lista:
        i = i.strip().lower()  
        encontrado = False
        for j in ocorrencias:
            if j[0] == i:
                j[1] += 1
                encontrado = True
                break
        if not encontrado:
            ocorrencias.append([i, 1])
    return ocorrencias

def verifica_palindromo(palavra):
    palavra_ao_contrario = palavra[::-1]
    if palavra == palavra_ao_contrario:
        return f"É um palíndromo!"
    return f"Não é um palíndromo!"

def percentual_vogais(frase):
    vogais = "aeiou"
    qtd_vogais = 0
    palavras2 = []
    palavras = frase.split()
    for i in palavras:
        letras = list(i)
        palavras2.extend(letras)
    for i in palavras2:
        if i in vogais:
            qtd_vogais += 1
    percentual = (qtd_vogais * 100) / len(palavras2)
    return percentual

def codificar_frase(frase):
    nova_frase = ''
    for i in frase:
        nova_frase += chr(ord(i) + 3)
    nova_frase = nova_frase[::-1]  
    frase_codificada = nova_frase[-1] + nova_frase[1:-1] + nova_frase[0]
    return frase_codificada

def decodificar_frase(frase):
    frase = frase[-1] + frase[1:-1] + frase[0]
    nova_frase = ''
    for i in reversed(range(len(frase))):
        nova_frase += frase[i]
    nova_frase2 =''
    for i in nova_frase:
        nova_frase2 += chr(ord(i) - 3)
    return nova_frase2