import Tree

t = Tree.Tree()

t.insere(2)
t.insere(3)
t.insere(1)
t.insere(12)

print("InOrdem:", end=' ')
print(t.inOrdem())
print("preOrdem:", end=' ')
print(t.preOrdem())
print("posOrdem:", end=' ')
print(t.posOrdem())

print("\nprintFolhas:", end=' ')
print(t.printFolhas())

print("\nSoma:", end=' ')
print(t.soma())

print("\nAltura da árvore:", end=' ')
print(t.altura())

print("\nAltura do Nó:", end=' ')
print(t.altura_no(12))