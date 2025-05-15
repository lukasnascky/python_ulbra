canal4 = 0
canal5 = 0
maior_audi = 0
maior_canal = ""
audi_tot = 0

canal_ass = int(input("Canal assistido: "))
while canal_ass == 4 or canal_ass == 5:
    audi = int(input("Audiência: "))
    if audi != 0:
        if canal_ass == 4:
            canal4 = canal4 + audi
        elif canal_ass == 5:
            canal5 = canal5 + audi
    audi_tot = audi_tot + audi
    canal_ass = int(input("Canal assistido: "))

if canal4 > maior_audi:
    maior_audi = canal4
    maior_canal = "Canal 4"
if canal5 > maior_audi:
    maior_audi = canal5
    maior_canal = "Canal 5"
per_canal5 = (canal5 / audi_tot) * 100

print("Maior canal: ", maior_canal)
print("Percentual Canal 5: ", per_canal5)