nome = input("Nome completo: ")
email = input("E-mail: ")

print(f"\nParabéns {nome}! Seu cadastro foi realizado com sucesso e você ganhou um cupom de desconto de 10% para a sua primeira compra na TecnoPlus.")

valor_compra = float(input("\nValor total da primeira compra: R$ "))

desconto = valor_compra * 0.1
compra_com_desconto = valor_compra - desconto

print(f"\nO valor total da sua compra é R$ {valor_compra}. Com o cupom de desconto você terá um desconto de R$ {desconto} e o valor final a ser pago será de R$ {compra_com_desconto}.")