tupla_vazia = () #não faz sentido pois seus dados são inalteraveis

tupla1 = (1,)
tupla2 = (1) 

print(len(tupla_vazia))
print(len(tupla1))
print(tupla2)


dados = (1, 2)
#dados[1] = 7 ---> o python não permite


pessoa = ("Fulano", "De Tal", 25)

nome, sobrenome, idade = pessoa

print("Nome: ",nome, sobrenome, "\nIdade: ", idade)


a = 1
b = 2

a, b = b, a
print(a, b)