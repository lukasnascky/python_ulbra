class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def inOrdem(self):
        if self.raiz != None:
            return self.raiz.inOrdem()

    #Imprimir todos os nós ancestrais do nó que contém valor.
    def print_ancestrais(self, valor):
        if self.raiz != None:
            self.raiz.print_ancestrais(valor)
            print() #serve unicamente para dar quebra de linha após finalizar
    
    #Imprimir todos os nós do menor caminho do nó raiz ao nó que contém valor.
    def print_caminho(self, valor):
        if self.raiz != None:
            self.raiz.print_caminho(valor)
            print()

    #Imprimir somente os nós que são nós internos e ancestrais do nó que contém valor.
    def print_ancestrais_internos(self, valor):
        if self.raiz != None:
            self.raiz.print_ancestrais_internos(valor)
            print()
    
    #Imprimir em ordem crescente todos os nós descendentes do nó que contém o maior valor da árvore.
    def print_descendentes_do_maior(self):
        if self.raiz != None:
            self.raiz.print_descendentes_do_maior()
            print()
    
    #Imprimir em ordem crescente todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore e que são menores que ele.
    def print_ida_ao_maior(self):
        if self.raiz != None:
            self.raiz.print_ida_ao_maior()
    
    #Retornar a soma de todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore.
    def soma_ida_ao_maior(self):
        if self.raiz != None:
            return self.raiz.soma_ida_ao_maior()


class No:
    def __init__(self, valor):
        self.info = valor
        self.dir = None
        self.esq = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None: 
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.inOrdem()
    
    #Imprimir todos os nós ancestrais do nó que contém valor.
    def print_ancestrais(self, valor):
        if valor < self.info:
            if self.esq != None:
                print(self.info, end=' ')
                self.esq.print_ancestrais(valor)
        elif valor > self.info:
            if self.dir != None:
                print(self.info, end=' ')
                self.dir.print_ancestrais(valor)
    
    #Imprimir todos os nós do menor caminho do nó raiz ao nó que contém valor.
    def print_caminho(self, valor):
        print(self.info, end=' ')
        if valor < self.info:
            if self.esq != None:
                self.esq.print_caminho(valor)
        else:
            if self.dir != None:
                self.dir.print_caminho(valor)

    #Imprimir somente os nós que são nós internos e ancestrais do nó que contém valor.
    def print_ancestrais_internos(self, valor): 
        if valor < self.info:
            if self.esq != None:
                print(self.info, end=' ')
                self.esq.print_ancestrais_internos(valor)
        elif valor > self.info:
            if self.dir != None:
                print(self.info, end=' ')
                self.dir.print_ancestrais_internos(valor)
    
    #Imprimir em ordem crescente todos os nós descendentes do nó que contém o maior valor da árvore.
    def print_descendentes_do_maior(self):
        if self.dir != None:
            self.dir.print_descendentes_do_maior()
        else:
            self.esq.inOrdem()
    
    #Imprimir em ordem crescente todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore e que são menores que ele.
    def print_ida_ao_maior(self):
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.print_ida_ao_maior()

    #Retornar a soma de todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore.
    def soma_ida_ao_maior(self):
        soma_total = self.info
        if self.dir != None:
            soma_total += self.dir.soma_ida_ao_maior()
        return soma_total