import time
import psutil
import os

arquivo = "Aula 01/numeros.txt"

numero_procurado = int(input("Digite o número que deseja buscar: "))


processo = psutil.Process(os.getpid())

inicio_tempo = time.perf_counter()
cpu_inicial = processo.cpu_times()
memoria_inicial = processo.memory_info().rss

with open(arquivo, 'r') as c:
    conteudo = c.read()
    lista_numeros = [int(valor) for valor in conteudo.split()]

encontrado = False

for numero in lista_numeros:
    if numero == numero_procurado:
        encontrado = True
        break

fim_tempo = time.perf_counter()
cpu_final = processo.cpu_times()
memoria_final = processo.memory_info().rss


tempo_execucao = fim_tempo - inicio_tempo
uso_cpu = (cpu_final.user - cpu_inicial.user) + (cpu_final.system - cpu_inicial.system)
uso_memoria = memoria_final - memoria_inicial

# Resultados
if encontrado:
    print(f"O número {numero_procurado} foi encontrado!")
else:
    print(f"O número {numero_procurado} não foi encontrado.")

print(f"\nEstatísticas de execução:")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print(f"Uso de CPU: {uso_cpu:.10f} segundos de CPU")
print(f"Consumo de memória: {uso_memoria / 1024:.2f} KB")