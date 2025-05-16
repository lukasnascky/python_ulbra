class PilhaE:
    
    
    def inserir_fim(self, valor): #Insere um valor ao final da lista
        self.vetor[self.quant] = valor
        self.quant += 1

    
    def remover_fim(self): #Remove um valor do final da lista
         self.quant -= 1


    def esta_cheia(self): #Verifica se a lista está cheia
         return self.quant >= self.tam
    

    def esta_vazia(self): #Verifica se a lista está vazia
         return self.quant == 0
    

    