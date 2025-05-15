def verifica_triangulo(x, y, z):
    if (x < y + z) or (y < x + z) or (z < x + y): 
        if (x == y) and (y == z):
            return f"\nTriângulo Equilátero."
        elif (x != y) and (y != z):
            return f"\nTriângulo Escaleno."
        else:
            return f"\nTriângulo Isósceles."
    else:
        return f"\nNão é um triângulo!"

x = float(input("Primeiro lado: "))
y = float(input("Segundo lado: "))
z = float(input("Terceiro lado: "))
print(verifica_triangulo(x, y, z))
#_#