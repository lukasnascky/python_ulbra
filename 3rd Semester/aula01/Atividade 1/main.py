import Frac

x = Frac.Frac(25, 20)
y = Frac.Frac(4, 3)

#print(x.num, x.den) --- não é pra fazer assim
#print(y.num, y.den) --- não é pra fazer assim

#print(x.get_num(), '/', x.get_den()) --- não fazer assim

z = x.mult(y) #multiplica x por y (num * num - den * den)
print("\nMultiplicação - x * y:")
z.show()

k = x.div(y) #multiplica y por x (num * num - den * den)
print("\nDivisão - x / y:")
k.show()


#Tarefa --- Implementar as funções soma, sub, div e simplifica
j = x.add(y)
print("\nAdição - x + y:")
j.show()


novo_x = x.simplifica()
print("Simplificação - x")
novo_x.show()


#l = x.sub(y)
#l.show()

