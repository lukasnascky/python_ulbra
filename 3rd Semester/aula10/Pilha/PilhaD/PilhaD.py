class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    

class PilhaD:
    def __init__(self):
        self.topo = None
        self.quant = 0
    
    #Insere um elemento no topo da pilha
    def push(self, valor):
        self.topo = No(valor, self.topo)
        self.quant += 1
    
    #Remove o elemento do topo da lista
    def pop(self):
        if not self.esta_vazia():
            self.topo = self.topo.prox
            self.quant -= 1
    
    #Verifica se a pilha está vazia e retorna boolean
    def esta_vazia(self):
        return self.quant == 0
    
    #Retorna o tamnaho atual da pilha
    def tamanho_atual(self):
        return self.quant

    #Retorna o topo da pilha
    def ver_topo(self):
        return self.topo.info
    
    #Imprime os valores na pilha de cima pra baixo
    def show(self):
        aux = self.topo
        for elemento in range(self.quant):
            print(aux.info, end=' ')
            aux = aux.prox
        print('')