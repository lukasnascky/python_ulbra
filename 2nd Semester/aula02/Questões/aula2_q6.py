def ordenar_valores(a, b, c):
    if a < b and a < c:
        if b < c:
            return f"{str(a)}, {str(b)}, {str(c)}"
        else:
            return f"{str(a)}, {str(c)}, {str(b)}"
    elif b < a and b < c:
        if a < c:
            return f"{str(b)}, {str(a)}, {str(c)}"
        else:
            return f"{str(b)}, {str(c)}, {str(a)}"
    else:
        if a < b:
            return f"{str(c)}, {str(a)}, {str(b)}"
        else:
            return f"{str(c)}, {str(b)}, {str(a)}"
    
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))
print(ordenar_valores(valor1, valor2, valor3))
#_#