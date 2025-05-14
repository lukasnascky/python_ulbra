print("---> SUA IDADE EM DIAS <---")
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

idade_em_dias = (anos * 365) + (meses * 30) + dias

print(f"\nIdade: {idade_em_dias} dias")