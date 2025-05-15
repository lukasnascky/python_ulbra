valor_hora = float(input("Valor da hora trabalhada: R$ "))
qtd_horas_semana = float(input("Quantidade de horas trabalhadas na semana: "))

salario_bruto = valor_hora * (qtd_horas_semana * 4.5)
desconto_imposto = salario_bruto * (float(input("Percentual de desconto com imposto: ")) / 100)

print("\n---FOLHA DE PAGAMENTO---")
print(f"Salário bruto: R${salario_bruto}\nValor desconto: R$ {desconto_imposto}\nSalário Líquido: {salario_bruto - desconto_imposto}")