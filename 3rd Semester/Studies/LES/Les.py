class Les:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir_fim(self, valor):
        if self.quant != self.tam_maximo:
            self.vetor[self.quant] = valor
            self.quant += 1
            return True
        return False

    def remover_fim(self):
        if self.quant != 0:
            self.quant -= 1
            return True
        return False

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()
    
    def esta_cheia(self):
        if self.quant == self.tam_maximo:
            return True
        return False
    
    def esta_vazia(self):
        if self.quant == 0:
            return True
        return False