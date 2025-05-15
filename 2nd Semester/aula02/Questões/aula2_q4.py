def media_notas(nota1, nota2, nota3, tipo_media):
    if tipo_media == "A":
        media = (nota1 + nota2 + nota3) / 3
    elif tipo_media == "P":
        media = ((nota1 * 5) + (nota2 * 3) + nota3 * 2) / 10
    return media

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
tipo_media = input("Tipo da média(A/P): ")
print(media_notas(n1, n2, n3, tipo_media))
#_#