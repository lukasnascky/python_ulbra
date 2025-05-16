class Tree:
    def __init__(self):
        self.raiz = None


    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
        
    
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    

    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
    

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
    

    #def busca_caminho(self, valor):
    #    if self.raiz == None:
    #        return False
    #    else:
    #        return self.raiz.busca_caminho(valor)
    

    #def busca_caminho_reverso(self, valor):
    #    if self.raiz == None:
    #        return False
    #    else:
    #        return self.raiz.busca_caminho_reverso(valor)


class No:
    def __init__(self, valor):
        self.dir = None
        self.info = valor
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
    
    #def busca(self, valor):
    #    if valor == self.info:
    #        return True
    #    elif valor < self.info:
    #        if self.esq == None:
    #            return False
    #        else:
    #            return self.esq.busca(valor)
    #    else:
    #        if self.dir == None:
    #            return False
    #        else:
    #            return self.dir.busca(valor)


    #def busca_caminho(self, valor):
    #    if valor == self.info:
    #        print(self.info)
    #        return True
    #    elif valor < self.info:
    #        if self.esq == None:
    #            return False
    #        else:
    #            print(self.info, end=' ')
    #            return self.esq.busca(valor)
    #    else:
    #        if self.dir == None:
    #            return False
    #        else:
    #            print(self.info, end=' ')
    #            return self.dir.busca(valor)
        

    #def busca_caminho_reverso(self, valor):
    #    if valor == self.info:
    #        print(self.info, end=' ')
    #    elif valor < self.info:
    #        if self.esq == None:
    #            return False
    #        else:
    #            self.esq.busca(valor)
    #            print(self.info, end=' ')
    #    else:
    #        if self.dir == None:
    #            return False
    #        else:
    #            self.dir.busca(valor)
    #            print(self.info, end=' ')
    

    #def busca_nivel(self, valor):
    #    if valor == self.info:
    #        return 1
    #    elif valor < self.info:
    #        if self.esq == None:
    #            return False
    #        else:
    #            return 1 + self.esq.busca(valor)
    #    else:
    #        if self.dir == None:
    #            return False
    #        else:
    #            return 1 + self.dir.busca(valor)


    #def busca(self, valor):
    #    if valor == self.info:
    #        return self.info
    #    elif valor < self.info:
    #        if self.esq == None:
    #            return False
    #        else:
    #            return self.info + self.esq.busca(valor)
    #    else:
    #        if self.dir == None:
    #            return False
    #        else:
    #            return self.info + self.dir.busca(valor)   
    

    def busca(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.busca(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.busca(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
    

    def inOrdem(self):

    
    #