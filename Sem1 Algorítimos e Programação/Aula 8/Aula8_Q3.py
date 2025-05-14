num_nasc = int(input("Número de crianças nascidas: "))
num_mortas = 0
menos_um = 0
masc = 0
sexo = input("Sexo(f ou m): ")
while (sexo == "f" or sexo == "m") and num_mortas <= num_nasc:
    idade = int(input("Meses de vida: "))
    num_mortas = num_mortas + 1
    if idade < 12:
        menos_um = menos_um + 1
    if sexo == "m" and idade >= 12:
        masc = masc + 1
    sexo = input("Sexo(f ou m): ")

per_mortes = (num_mortas / num_nasc) * 100
print("Percentual de mortes: ", per_mortes, "%")
print("Quantidade mortes antes de 1 ano:", menos_um)
print("Quantidade sexo masculino:", masc)