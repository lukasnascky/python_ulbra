valor1 = int(input("Valor: "))
if valor1 >= 10:
    print("O valor tem que ser menor que 10!")
produto = valor1 
inter = 0
while produto < 1000:
    produto = produto * 3
    inter = inter + 1
print("Produto:", produto)
print("Interações:", inter)