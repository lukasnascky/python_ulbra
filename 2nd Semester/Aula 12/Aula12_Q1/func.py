def insere_usuario(dicionario, login, nome, ult_acesso, maquina):
    dicionario[login] = {"nome": nome, "ult_acesso": ult_acesso, "maquina": maquina}
    return dicionario
    
def altera_login(usuarios, login):
    if login in usuarios:
        alterador = input("O que deseja alterar?\ntudo | nome | ult_acesso | maquina\n>>>")
        if alterador == 'nome'or alterador == 'tudo':
            nome = input("Nome: ")
            usuarios[login]['nome'] = nome

        if alterador == 'ult_acesso'or alterador == 'tudo':
            ult_acesso = input("Ultimo acesso: ")
            usuarios[login]['ult_acesso'] = ult_acesso

        if alterador == 'maquina'or alterador == 'tudo':
            maquina = input("Máquina: ")
            usuarios[login]['maquina'] = maquina

        return usuarios
    return f"O usuário solicitado não existe!"