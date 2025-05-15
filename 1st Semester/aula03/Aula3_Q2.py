base = float(input("Base: "))
altura = float(input("Altura: "))

if base == altura:
    print("Quadrado perfeito")
else:
    print("\nRetângulo")
    if base > altura:
        print("Base é maior -", base)
    else:
        print("Altura é maior -", altura)