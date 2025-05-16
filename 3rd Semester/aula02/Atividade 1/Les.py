class Les:
    def __init__(self, tamanho): 
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
    
    def inserir_inicio(self, valor): #Insere um valor ao inicio da lista
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i-1]
        self.vetor[0] = valor
        self.quant += 1

    def remover_inicio(self): #Remove um valor do inicio da lista
        for i in range(self.quant-1):
            self.vetor[i] = self.vetor[i+1]
        self.quant -= 1

    def inserir_fim(self, valor): #Insere um valor ao final da lista
        self.vetor[self.quant] = valor
        self.quant += 1

    def remover_fim(self): #Remove um valor do final da lista
         self.quant -= 1
    
    def remover_valor(self, valor): #Remove o valor especificado da lista
        for i in range(self.quant):
            if self.vetor[i] == valor:
                for i in range(self.quant-1):
                    self.vetor[i+1] = self.vetor[i+2]
                self.quant -= 1
                return True
        return False

    def show(self): #Imprime a lista
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print("")

    def esta_cheia(self): #Verifica se a lista está cheia
         return self.quant >= self.tam
    
    def esta_vazia(self): #Verifica se a lista está vazia
         return self.quant == 0
    
    def get_quant(self): #Retorna a quantidade de itens da lista
        return self.quant

    def get_tam(self): #Retorna o tamanho da lista
        return self.tam
    
    def get_first(self): #Retorna o primeiro valor da lista
        return self.vetor[0]
    
    def get_last(self): #Retorna o ultimo valor da lista
        return self.vetor[self.quant-1]