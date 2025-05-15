def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]

def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False
    return True

def escrever_relatorio(ips_validos, ips_invalidos, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo:
        arquivo.write("[Endereços válidos:]\n")
        for ip in ips_validos:
            arquivo.write(ip + '\n')
        arquivo.write("\n[Endereços inválidos:]\n")
        for ip in ips_invalidos:
            arquivo.write(ip + '\n')

def gerar_relatorio_ips(nome_arquivo_entrada, nome_arquivo_saida):
    ips = ler_arquivo(nome_arquivo_entrada)
    ips_validos = []
    ips_invalidos = []

    for ip in ips:
        if validar_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

    escrever_relatorio(ips_validos, ips_invalidos, nome_arquivo_saida)