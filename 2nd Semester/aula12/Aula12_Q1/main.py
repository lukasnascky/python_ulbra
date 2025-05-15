from func import *

usuarios = {"mickey": {"nome": "Mickey Mouse", "ult_acesso": "12/01/2024", "maquina": "labin05"},
            "donald": {"nome": "Donald Duck", "ult_acesso": "23/01/2024", "maquina": "labin06"},
            "minnie": {"nome": "Minerva Mouse", "ult_acesso": "24/01/2024", "maquina": "labin11"},
            "sofia": {"nome": "Sofia Sofista", "ult_acesso": "01/02/2024", "maquina": "labin12"},
            "marcos": {"nome": "Marcos Malauke", "ult_acesso": "12/01/2024", "maquina": "labin08"}}

while True:
    menu = int(input('''
1. Inserir usuário:
2. Listar os nomes de todos os usuários
3. Listar dados de um usuário
4. Listar os nomes dos usuários com último acesso em uma data específica
5. Alterar dados de um usuário: 
6. Excluir um usuário
0. sair
>>>'''))
    if menu == 0:
        break

    elif menu == 1: #insere um novo usuário ao dicionário
        login = input("\nLogin: ")
        if login in usuarios:
            print("O usuário solicitado já existe!")
        else:
            nome = input("Nome: ")
            ult_acesso = input("Ultimo acesso: ")
            maquina = input("Máquina: ")
            usuarios = insere_usuario(usuarios, login, nome, ult_acesso, maquina)

    elif menu == 2: #lista os nomes de todos os usuários
        print("\nNOMES")
        for valor in usuarios.values():
            print(f"Nome: {valor['nome']}")
    
    elif menu == 3: #lista dados de um usuário
        login = input("\nLogin: ")
        if login not in usuarios:
            print("O usuário solicitado não existe!")
        else:
            print(f"Login: {login} \t| Nome: {usuarios[login]['nome']} \t| Ultimo acesso: {usuarios[login]['ult_acesso']} \t| Máquina: {usuarios[login]['maquina']}")

    elif menu == 4: #Lista os nomes dos usuários com último acesso em uma data específica
        ult_acesso = input("\nUltimo acesso desejado: ")
        for login, valor in usuarios.items():
            if ult_acesso == valor['ult_acesso']:
                print(f"Login: {login} \t| Nome: {valor['nome']} \t| Ultimo acesso: {valor['ult_acesso']} \t| Máquina: {valor['maquina']}")
    
    elif menu == 5: #altera dados de um usuário
        login = input("\nLogin: ")
        usuarios = altera_login(usuarios, login)

    elif menu == 6: #excluir um usuário
        login = input("\nLogin: ")
        if login in usuarios:
            usuarios.pop(login)