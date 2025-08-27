class Les:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir_fim(self, valor):
        if not self.esta_cheia():
            self.vetor[self.quant] = valor
            self.quant += 1
            return True
        return False

    def remover_fim(self):
        if not self.esta_vazia():
            self.quant -= 1
            return True
        return False

    def inserir_inicio(self, valor):
        if not self.esta_cheia():
            for i in range(self.quant, 0, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[0] = valor
            self.quant += 1
            return True
        return False

    def remover_inicio(self):
        if not self.esta_vazia():
            for i in range(self.quant-1):
                self.vetor[i] = self.vetor[i + 1]
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
    
    def ver_primeiro(self):
        return self.vetor[0]
    
    def ver_ultimo(self):
        return self.vetor[self.quant - 1]
    
    def tamanho_atual(self):
        return self.quant
    
    def capacidade(self):
        return self.tam_maximo
    