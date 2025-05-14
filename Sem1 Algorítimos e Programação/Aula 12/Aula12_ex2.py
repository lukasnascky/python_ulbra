listaPrecos = [15, 20, 10, 25, 30, 5]
listaProdutos = ['Boneca', 'Camiseta', 'Chaveiro', 'Caneta', 'Copo']
i = 5
while i >= 0:
    if listaPrecos[i-1] > listaPrecos[i]:
        print('Mais caro:', listaProdutos[i-1])
    else:
        print('Mais caro:', listaProdutos[i])
    i = i - 1