class FilaE:
    def __init__(self, tamanho): 
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
    

    def inserir(self, valor): #Insere um valor
        self.vetor[self.quant] = valor
        self.quant += 1


    def remover(self): #Remove um valor
        for i in range(self.quant-1):
            self.vetor[i] = self.vetor[i+1]
        self.quant -= 1


    def ver_primeiro(self):
        return self.vetor[0] 


    def esta_cheia(self): #Verifica se a fila está cheia
         return self.quant >= self.tam
    

    def esta_vazia(self): #Verifica se a fila está vazia
         return self.quant == 0


    def show(self): #Imprime a lista
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print("")
    
    