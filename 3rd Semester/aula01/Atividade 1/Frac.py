#Cria uma classe
class Frac:
    def __init__(self, numera, denomina): #__init__ é o contrutor
        self.num = numera
        self.den = denomina

    def get_num(self): #pega o valor do numerador
        return self.num
    
    def get_den(self): #pega o valor do denominador
        return self.den
    
    def show(self): #imprime a fração armazenada
        print(self.num, '/', self.den)

    def mult(self, valor): #retorna a mutiplicação das frações
        n = self.num * valor.get_num()
        d = self.den * valor.get_den()
        resultado = Frac(n, d)
        return resultado
    
    def div(self, valor): #retorna a divisão das frações
        n = self.num * valor.get_den()
        d = self.den * valor.get_num()
        resultado = Frac(n, d)
        return resultado
    
    def add(self, valor): #retorna a adição das frações
        if self.den == valor.get_den():
            n = self.num + valor.get_num()
            d = self.den
        else:
            n = (self.den * valor.get_num()) + (valor.get_den() * self.num)
            d = self.den * valor.get_den()
        resultado = Frac(n, d)
        return resultado
    
    def sub(self, valor): #retorna a subtração das frações
        pass
    
    #def simplifica(self): #simplifica uma fração
    #    n, d = self.num, self.den
    #    cont = 1
    #    for i in range(10):
    #        if (self.num % cont == 0) and (self.den % cont == 0):
    #            n = int(self.num / cont)
    #            d = int(self.den / cont)
    #        resultado = Frac(n, d)
    #        cont += 1
    #    return resultado
    
    def simplifica(self): #simplifica uma fração
        n, d = self.num, self.den
        cont = 2
        while True:
            if 
            if (self.num % cont == 0) and (self.den % cont == 0):
                n = int(self.num / cont)
                d = int(self.den / cont)
            if cont > 9:
                cont == 1
            resultado = Frac(n, d)
            cont += 1
        return resultado