def identifica_sinal(valor1):
    if valor1 >= 0:
        return f"O valor {valor1} é positivo!"
    else:
        return f"O valor {valor1} é negativo!"

num1 = int(input("Digite um número: "))
print(identifica_sinal(num1))
#_#