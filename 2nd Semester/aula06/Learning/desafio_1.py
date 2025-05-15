def verifica_maior_aparicoes(lista):    
    maior_num = None
    qtd_vezes = 0

    for x in lista:
        contagem = lista.count(x)
        if contagem > qtd_vezes:
            maior_num = x
            qtd_vezes = contagem
    return maior_num, qtd_vezes

lista = [1, 2, 3, 3, 5, 3, 4, 5, 9, 1]

print(verifica_maior_aparicoes(lista))