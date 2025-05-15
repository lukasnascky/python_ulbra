cont = 0
m_imc = 999

while cont < 10:
    nome = input("\nNome: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso / altura ** 2
    if imc < m_imc:
        m_imc = imc
    if imc < 18.5:
        print("Abaixo do peso!")
    elif imc < 25:
        print("Peso normal!")
    elif imc < 30:
        print("Acima do peso!")
    else:
        print("Obesidade!")
    cont = cont + 1
print("\nMenor IMC:", m_imc, "\nNome:", nome)