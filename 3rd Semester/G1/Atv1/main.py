import Ldde

l = Ldde.Ldde()

l.inserir_inicio('D')
l.inserir_fim('B')
l.inserir_fim('A')
l.inserir_fim('A')
l.inserir_fim('A')

l.show()

l.remove_duplicatas_do_valor('A')
l.show()