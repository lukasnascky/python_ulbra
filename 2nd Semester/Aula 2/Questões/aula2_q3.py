def valor_par_impar(valor1):
    if valor1 % 2 == 0:
        return f"O valor {valor1} é par!"
    else:
        return f"O valor {valor1} é impar!"

num1 = int(input("Digite um número: "))
print(valor_par_impar(num1))
#_#