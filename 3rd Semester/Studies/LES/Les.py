class Les:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir_fim(self, valor):
        if self.quant == self.tam_maximo:
            print("A lista está cheia!")
        else:
            self.vetor[self.quant] = valor
            self.quant += 1

    def remover_fim(self):
        if self.quant == 0:
            print("A lista está vazia!")
        else:
            self.quant -= 1

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()
    