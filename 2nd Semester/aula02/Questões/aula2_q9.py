def calcula_peso_ideal(alt, sexo):
    if sexo == "m":
        peso_ideal = (72.7 * alt) - 58
    elif sexo == "f":
        peso_ideal = (62.1 * alt) - 44.7
    return peso_ideal

altura = float(input("Altura: "))
sexo = input("Sexo(m/f): ")
print(f"Peso ideal: {calcula_peso_ideal(altura, sexo)}Kg")
#_#