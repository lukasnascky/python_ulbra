from funcoes_q6 import *

print("""Qual o melhor Sistema Operacional para uso em servidores?
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro""")

lista_votacao = []
num_sistema = int(input("Digite o sistema desejado: (0=fim): "))
while num_sistema != 0:
    if num_sistema < 0 or num_sistema > 6:
        print("Coloque um valor válido (De 1 a 6): ")
    else:
        lista_votacao.append(num_sistema)
    num_sistema = int(input("Digite o sistema desejado: (0=fim): "))

total_votacao = len(lista_votacao)
(windows, unix, linux_melhor_sistema, netware, maclixo, outro) = computaVotos(lista_votacao)

print(f'''
Sistema Operacional      Votos    %
--------------------------- ------- ---
Windows Server          {windows}       {(windows/total_votacao)*100:.2f}%
Unix                    {unix}      {(unix/total_votacao)*100:.2f}%
Linux                   {linux_melhor_sistema}      {(linux_melhor_sistema/total_votacao)*100:.2f}%
Netware                 {netware}       {(netware/total_votacao)*100:.2f}%
Mac OS                  {maclixo}       {(maclixo/total_votacao)*100:.2f}%
Outro                   {outro}       {(outro/total_votacao)*100:.2f}%
--------------------------- -----
Total                   {total_votacao}
''')


print(f'''
Sistema Operacional      Votos    %
--------------------------- ------- ---
Windows Server          {windows}       {(windows/total_votacao)*100:.2f}%
Unix                    {unix}      {(unix/total_votacao)*100:.2f}%
Linux                   {linux_melhor_sistema}      {(linux_melhor_sistema/total_votacao)*100:.2f}%
Netware                 {netware}       {(netware/total_votacao)*100:.2f}%
Mac OS                  {maclixo}       {(maclixo/total_votacao)*100:.2f}%
Outro                   {outro}       {(outro/total_votacao)*100:.2f}%
--------------------------- -----
Total                   {total_votacao}
''')