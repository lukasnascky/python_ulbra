#Entrada
pco_ing = float(input("Valor do ingreço: R$"))
prof = input("Profissão: ")
idade = int(input("Idade: "))
desc_prof = 0
desc_idade = 0

#Processos
if prof == "professor" or prof == "estudante":
   desc_prof = pco_ing / 2
elif prof == "bombeiro":
    desc_prof = 15
elif prof == "artista profissional":
    desc_prof = 10
else:
    desc_prof = 0

if idade >= 60 or idade <= 10:
    desc_idade = 20
else:
    desc_idade = 0

#Saida
print("Valor ingresso: R$", pco_ing - desc_prof - desc_idade)