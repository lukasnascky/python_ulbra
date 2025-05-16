class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    
class Ldse:
    def __init__(self): #Sem o ult
        self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = No(valor, None)
        else:
            aux = self.prim
            while aux.prox != None:
                aux = aux.prox
            aux.prox = No(valor, None)
        self.quant += 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = None
        else:
            aux = self.prim
            while aux.prox.prox != None:
                aux = aux.prox
            aux.prox = None
        self.quant -= 1

    def remover_valor(self, valor):
        if self.quant == 1 and valor == self.prim.info:
            self.prim = None
        else:
            aux = self.prim
    
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end= ' ')
            aux = aux.prox
        print('')