maior_peso = 0
mat_maior = ''
peso_tit = 0
peso_inox = 0
peso_alu = 0

peso_mat = float(input("Peso do material: "))
while peso_mat != 0:
    material = input("Material(t - Titânio, i - Inox, a - Alumínio): ")
    if material == "t":
        peso_tit = peso_mat * 6
        print(peso_mat, "Kg de titânio: R$", peso_tit)
    elif material == "i":
        peso_inox = peso_mat * 6
        print(peso_mat, "Kg de inox: R$", peso_inox)
    elif material == "a":
        peso_alu = peso_mat * 9
        print(peso_mat, "Kg de alumínio: R$", peso_alu)
    if peso_mat > maior_peso:
        maior_peso = peso_mat
        mat_maior = material
    peso_mat = float(input("Peso do material: "))

print("Material mais vendido em peso:", material, " ", maior_peso, "Kg")