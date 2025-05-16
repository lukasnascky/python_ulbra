#LISTA DINAMICA SIMPLESMENTE ENCADEADA
##LINKED LIST

class No: #Cria um Nó
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1
    
    def remover(self, valor): #usar 2 variaveis aux
        if self.quant == 1 and self.prim.info == valor:
            self.prim = self.ult = No(valor, None)
            self.quant -= 1
        else:
            if self.
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end='')
            aux = aux.prox
        print()