class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
    
class Lee:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.quant = 0
        self.prox_pos_vazio = self.inicializa_estrutura()
        self.prox = -1
        self.ult = -1

    def inicializa_estrutura(self):
        for i in range(self.tam_maximo - 1):
            self.vetor[i] = No(None, i + 1)
        self.vetor[self.tam_maximo - 1] = No(None, -1)
        return 0
    
    def ocupa_no(self, valor, proximo):
        posicao_livre = self.prox_pos_vazio
        self.prox_pos_vazio = self.vetor[self.prox_pos_vazio].prox
        self.vetor[posicao_livre] = No(valor, proximo)
        return posicao_livre
    
    def inserir_incio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1
        else:
            self.prim = self.ocupa_no(valor, self.prim)
            self.quant += 1

    