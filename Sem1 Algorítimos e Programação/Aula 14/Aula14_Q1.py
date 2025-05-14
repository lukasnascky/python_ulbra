cont = 1
senha = input("Senha: ")
#ACESSO NEGADO
while senha != "algoritmos1":
    print("ACESSO NEGADO!")
    cont = cont + 1
    senha = input("\nSenha: ")
#ACESSO PERMITIDO
print("ACESSO PERMITIDO!\nQuantidades de tentativas:", cont)
#_#