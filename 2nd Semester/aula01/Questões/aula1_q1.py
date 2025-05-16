soma_dos_valores = 0
for i in range(5):
    soma_dos_valores += float(input("Digite um valor: "))
    i += 1

media = (soma_dos_valores) / 5

print(f"\nMédia: {media}")