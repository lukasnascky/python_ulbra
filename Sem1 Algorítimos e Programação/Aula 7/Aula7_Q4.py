cont = 0
sgost = 0
ngost = 0

qtd = int(input("Quantidade de pessoas: "))
while cont < qtd:
    like = input("Gostou da apresentação? (sim ou não) ")
    if like == "sim":
        sgost = sgost + 1
    elif like == "não":
        ngost = ngost + 1
    cont = cont + 1
if sgost > ngost:
    print("A maioria das pessoas gostaram da apresentação!")
elif ngost > sgost:
    print("A maioria das pessoas não gostaram da apresentação!")
else:
    print("Empate!")