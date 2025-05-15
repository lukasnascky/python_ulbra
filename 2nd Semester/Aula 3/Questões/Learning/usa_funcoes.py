from funcoes import *

print("-" * 60)
print('''    1. Verifica se um número é positivo ou negativo(bool)
    2. Verifica se um número é positivo ou negativo
    3. Verifica se um número é ímpar ou par
    4. Calcula média ponderada ou aritmética
    5. Converte idade em dias totais
    6. Ordena valores em ordem crescente
    7. Converte segundos em "horas:minutos:segundos"
    8. Verifica se um valor é perfeito
    9. Verifica o peso ideal 
    10. Verifica triângulo
    0. sair''')

menu = int(input(">>> "))
while menu != 0:
    if menu == 1:
        print("-" * 60)
        num1 = int(input("Valor inteiro: "))
        print(identifica_sinal_bool(num1))

    elif menu == 2:
        print("-" * 60)
        num1 = int(input("Digite um número: "))
        print(identifica_sinal(num1))

    elif menu == 3:
        print("-" * 60)
        num1 = int(input("Digite um número: "))
        print(valor_par_impar(num1))

    elif menu == 4:
        print("-" * 60)
        n1 = float(input("Primeira nota: "))
        n2 = float(input("Segunda nota: "))
        n3 = float(input("Terceira nota: "))
        tipo_media = input("Tipo da média(A/P): ")
        print(media_notas(n1, n2, n3, tipo_media))

    elif menu == 5:
        print("-" * 60)
        anos = int(input("Anos: "))
        meses = int(input("Meses: "))
        dias = int(input("Dias: "))
        print(f"Sua idade em dias é: {idade_em_dias(anos, meses, dias)} dias")

    elif menu == 6:
        print("-" * 60)
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
        valor3 = int(input("Terceiro valor: "))
        print(ordenar_valores(valor1, valor2, valor3))

    elif menu == 7:
        print("-" * 60)
        segundos = int(input("Segundos: "))
        print(segundos_para_tempo(segundos))

    elif menu == 8:
        print("-" * 60)
        num = int(input("Digite um número: "))
        print(verifica_num_perfeito(num))

    elif menu == 9:
        print("-" * 60)
        altura = float(input("Altura: "))
        sexo = input("Sexo(m/f): ")
        print(f"Peso ideal: {calcula_peso_ideal(altura, sexo)}Kg")

    elif menu == 10:
        print("-" * 60)
        x = float(input("Primeiro lado: "))
        y = float(input("Segundo lado: "))
        z = float(input("Terceiro lado: "))
        print(verifica_triangulo(x, y, z))

    else:
        print("-" * 60)
        print("Opção inválida!")

    print("-" * 60)
    menu = int(input(">>> "))
print("-" * 60)