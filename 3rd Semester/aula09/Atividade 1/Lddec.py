class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

 
class Lddec:
    def __init__(self):
        self.prim = None
        self.quant = 0

    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = No(None, valor, None)
            self.quant += 1
        else:
            aux = self.prim
            while aux != None and aux.prox!= self.prim:
                aux = aux.prox
            self.prim = No(aux, valor, self.prim)
            self.quant += 1

    def show_reverso(self):
        pass