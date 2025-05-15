cont = 0
m_maior = 0
mds = 0
idadetot = 0

while cont < 15:
    idade = int(input("\nIdade: "))
    nacio = input("País de origem: ")
    sexo = input("Sexo(M = masculino |F = feminino): ")
    if sexo == "F" and idade >= 18:
        m_maior = m_maior + 1
    if sexo == "M" and nacio == "Brasil" and (idade >= 20 and idade <= 30):
        mds = mds + 1
    idadetot = idadetot + idade
    cont = cont + 1
print("\nMulheres de maior:", m_maior)
print("Homens brasileiros entre 20 e 30 anos:", mds)
print("Média das idades: ", idadetot / cont)