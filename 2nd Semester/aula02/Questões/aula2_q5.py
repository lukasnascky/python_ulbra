def idade_em_dias(anos, meses, dias):
    idade = (anos * 360) + (meses * 30) + dias
    return idade

anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))
print(f"Sua idade em dias é: {idade_em_dias(anos, meses, dias)} dias")
#_#