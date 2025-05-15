cont = 0
m_peso = 0

while cont < 10:
    peso = float(input("Peso: "))
    if peso > m_peso:
        m_peso = peso
    cont = cont + 1
print("Maior peso:", m_peso, "Kg")