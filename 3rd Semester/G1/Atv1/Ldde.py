class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim = self.prim.ant
        self.quant -= 1
    
    def remove_duplicatas_do_valor(self, valor):
        prim_aparicao = True #Declara uma variável booleana para encontrar o primeiro valor
        aux = self.prim #Declara uma variável aux que recebe a posição do primeiro elemento da lista para percorre-la
        for i in range(self.quant): #Inicia um 'for' para percorrer a lista 
            if aux.info == valor: #Verifica se o valor da variável aux é igual ao valor passado como parametro
                if prim_aparicao == True: #Verifica se a variável prim_aparicao 
                    prim_aparicao = False 
                elif aux.info == valor and aux == self.ult:
                    self.ult = self.ult.ant
                    self.ult.prox = None
                    self.quant -= 1
                else:
                    aux.ant.prox = aux.prox
                    aux.prox.ant = aux.ant
                    self.quant -= 1
            aux = aux.prox
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info, end=' ')
            aux = aux.prox
        print('')  