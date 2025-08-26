import Les

lista = Les.Les(5)

lista.inserir_fim(1)
lista.show()

lista.inserir_fim(3)
lista.show()

lista.inserir_fim(5)
lista.show()

lista.inserir_fim(6)
lista.show()

lista.inserir_fim(9)
lista.show()


lista.remover_fim()
lista.show()


lista.inserir_fim(23)
lista.show()

print(f"Remover um elemento: {lista.remover_fim()}")
print(f"Remover um elemento: {lista.remover_fim()}")
print(f"Remover um elemento: {lista.remover_fim()}")
print(f"Remover um elemento: {lista.remover_fim()}")
print(f"Remover um elemento: {lista.remover_fim()}")
print(f"Remover um elemento: {lista.remover_fim()}") # aqui ele retornará False porque não há mais elementos a serem removidos