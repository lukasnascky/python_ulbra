import Ldde

lista = Ldde.Ldde()

lista.inserir_fim('A')
lista.inserir_inicio('B')
lista.inserir_inicio('C')

lista.show()
lista.show_inverso()
print(lista.tamanho_atual())

print()
lista.remover_fim()
lista.show()

lista.remover_inicio()
lista.show()
print(lista.tamanho_atual())