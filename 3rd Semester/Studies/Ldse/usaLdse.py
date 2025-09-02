import Ldse

lista = Ldse.Ldse()

lista.inserir_fim('C')
lista.inserir_inicio('B')
lista.inserir_inicio('A')
lista.show()

lista.inserir_fim('D')
lista.show()

lista.remover_fim()
lista.show()