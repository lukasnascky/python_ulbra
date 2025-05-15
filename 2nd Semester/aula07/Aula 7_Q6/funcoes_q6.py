def computaVotos(lista_votacao): 
    lista_votacao = lista_votacao[:]
    
    sistemas = []
    for i in range(1,7):
        sistemas.append(lista_votacao.count(i))
    return [ qtd_votos for qtd_votos in sistemas]