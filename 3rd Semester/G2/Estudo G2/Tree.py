class Tree:
    def __init__(self):
        self.raiz = None
    
    #Verifica se a arvore esta vazia e cria um No
    #Chama função para encontrar o lugar certo do No
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    
    #Busca um valor e retorna True ou False
    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    
    #InOrdem
    def inOrdem(self):
        if self.raiz != None:
            return self.raiz.inOrdem()
    
    #preOrdem
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
    
    #posOrdem
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()

    #printFolhas
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    #soma
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    
    #somaFolhas
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
    
    #Altura
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

    #a
    def altura_no(self, valor):
        if self.raiz != None:
            return self.raiz.altura_no(valor)


#=========================================================================#
class No:
    def __init__(self, valor):
        self.info = valor
        self.dir = None
        self.esq = None
    
    #Encontra o lugar certo e insere o No
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
    
    #Busca um valor em um No da arvore
    def busca(self, valor):
        if self.info == valor:
            return True
        elif self.info < valor:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    
    #InOrdem
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.inOrdem()
    
    #preOrdem
    def preOrdem(self):
        print(self.info, end=' ')
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()
    
    #posOrdem
    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info, end=' ')

    #Imprime todas as folhas da arvore percorrendo de maneita inOrdem
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info, end=' ')
        if self.dir != None:
            self.dir.printFolhas()

    #Soma todos os nos
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    #somaFolhas
    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total += self.info   

    #Encontra a altura da arvore
    def altura(self):
        hesq = hdir = -1
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)
    
    #altura do no
    def altura_no(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.altura_no(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.altura_no(valor)