def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(espaco_utilizado, espaco_total):
    return (espaco_utilizado / espaco_total) * 100

def ler_arquivo(nome_arquivo):
    usuarios = []
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        login, espaco = linha.strip().split(';')
        espaco = int(espaco)
        usuarios.append((login, espaco))
    arquivo.close()
    return usuarios

def gerar_relatorio(usuarios, nome_arquivo_saida, top_n=None):
    espaco_total = 0
    for usuario in usuarios:
        espaco_total += usuario[1]

    espaco_total_mb = bytes_para_mb(espaco_total)
    
    usuarios_mb = []
    for usuario in usuarios:
        login = usuario[0]
        espaco_em_mb = bytes_para_mb(usuario[1])
        percentual = calcular_percentual(usuario[1], espaco_total)
        usuarios_mb.append((login, espaco_em_mb, percentual))

    # Ordena os usuários pelo percentual de uso em ordem decrescente
    for i in range(len(usuarios_mb)):
        for j in range(i + 1, len(usuarios_mb)):
            if usuarios_mb[i][2] < usuarios_mb[j][2]:
                usuarios_mb[i], usuarios_mb[j] = usuarios_mb[j], usuarios_mb[i]

    if top_n is not None:
        usuarios_mb = usuarios_mb[:top_n]

    arquivo = open(nome_arquivo_saida, 'w')
    arquivo.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    arquivo.write("--------------------------------------------------------------\n")
    arquivo.write("Nr. Usuário Espaço utilizado % do uso\n\n")

    for i in range(len(usuarios_mb)):
        usuario = usuarios_mb[i]
        arquivo.write(f"{i + 1} {usuario[0]:<10} {usuario[1]:>10.2f} MB {usuario[2]:>10.2f}%\n")

    espaco_medio = espaco_total_mb / len(usuarios)

    arquivo.write("\n")
    arquivo.write(f"Espaço total ocupado: {espaco_total_mb:.2f} MB\n")
    arquivo.write(f"Espaço médio ocupado: {espaco_medio:.2f} MB\n")
    arquivo.close()