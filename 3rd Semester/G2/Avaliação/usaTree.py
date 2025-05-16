import Tree

t = Tree.Tree()

t.insere(4)
t.insere(3) 
t.insere(7)
t.insere(2)
t.insere(1)
t.insere(6)
t.insere(5)
t.insere(11)
t.insere(10)
t.insere(9)

t.print_ancestrais(6)
t.print_ancestrais(13)

print("\nInternos:")
t.print_ancestrais_internos(6)

print("\nDescendentes do maior: ")
t.print_descendentes_do_maior()

print("\nCaminho:")
t.print_caminho(6)

print("\nPrint ida ao maior :")
t.print_ida_ao_maior()

print("\nSoma ida ao maior :")
print(t.soma_ida_ao_maior())