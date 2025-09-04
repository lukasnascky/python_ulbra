import FilaE

fila = FilaE.FilaE(5)

print(fila.esta_vazia())
print(fila.esta_cheia())

fila.inserir('A')
fila.inserir('B')
fila.inserir('C')
fila.inserir('D')
fila.inserir('E')
fila.show()

print(fila.esta_cheia())

print(fila.ver_primeiro_elemento())
fila.remover()
print(fila.ver_primeiro_elemento())

fila.show()