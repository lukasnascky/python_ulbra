objetos = open('objetos.txt', 'r')
lista_objetos = objetos.read().split(',')
objetos.close()

objetos2 = open('objetos2.txt', 'w')
dic_objetos = {}
maior_qtd = 0
objeto_maior = ''
for objeto in lista_objetos:
    if objeto.lower() not in dic_objetos:
        cont = lista_objetos.count(objeto)
        if cont > maior_qtd:
            maior_qtd = cont
            objeto_maior = objeto
        dic_objetos[objeto.lower()] = cont
        objetos2.write(objeto.lower() + ':')
        objetos2.write(str(cont) + '\n')

objetos2.write(f'\nO objeto que aparece em maior quantidade e o(a) {objeto_maior}.')
objetos2.close()