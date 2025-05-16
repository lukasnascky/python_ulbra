class No:
    def __init__ (self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldsec:
    def __init__(self):
        self.prim = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 