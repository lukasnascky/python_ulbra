import Les
l = Les.Les(5)

l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")

print("\nDepois de adcinar um valor no começo")
l.inserir_inicio("G")
l.show()

print("\nDepois de remover um valor")
l.remover_inicio()
l.show()

print("\nAntes de remover fim")
l.show()

l.remover_fim()
print("\nDepois de remover fim")
l.show()

l.inserir_fim("D")
print("\nDepois de inserir fim")
l.show() 

print("\nImprime o primeiro elemento da lista")
print(l.get_first())

print("\nImprime o ultimo elemento da lista")
print(l.get_last())

print("\nDepois de remover o valor 'B' da lista")
print(f"Status: {l.remover_valor('B')}")
l.show()