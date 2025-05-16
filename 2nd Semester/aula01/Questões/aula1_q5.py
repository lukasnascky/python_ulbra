import random

while True:
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    print("\nAdivinhe o número entre 0 e 100!")

    palpite = -1  # Valor inicial qualquer diferente do número secreto

    while palpite != numero_secreto:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("\nO número é maior que isso.")
        elif palpite > numero_secreto:
            print("\nO número é menor que isso.")
        else:
            print("****************************************")
            print(f"Parabéns!!!! O número correto é {numero_secreto}")
            print(f"Quantidade de tentativas --> {tentativas}")
            print("****************************************")

    jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        print("\nObrigado por jogar! Até a próxima.")