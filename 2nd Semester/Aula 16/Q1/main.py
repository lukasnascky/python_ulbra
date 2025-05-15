import func

nome_arquivo_entrada = 'enderecos_ip.txt'
nome_arquivo_saida = 'relatorio_ips.txt'

func.gerar_relatorio_ips(nome_arquivo_entrada, nome_arquivo_saida)

print(f'Relatório gerado no arquivo: {nome_arquivo_saida}')