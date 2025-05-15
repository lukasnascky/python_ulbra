from funcoes_q4 import *

while True:
    atleta = input("\nAtleta: ")
    if atleta == "":
        break
    saltos_bau = ["Primeiro salto", "Segundo salto", "Terceiro salto", "Quarto salto", "Quinto salto"]
    saltos = []

    for i in saltos_bau:
        print(i)
        alt_salto = float(input(">>>"))
        saltos.append(alt_salto)
    
    print(f"\nResultado final: \nAtleta: {atleta}")
    print(f"Saltos: {saltos[0]}m - {saltos[1]}m - {saltos[2]}m - {saltos[3]}m - {saltos[4]}m")
    print(f"Media dos saltos: {media_saltos(saltos)}m")