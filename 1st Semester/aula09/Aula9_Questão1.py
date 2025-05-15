massa = float(input("Massa Inicial: "))
horas = 0
min = 0
seg = 0

while massa >= 0.5:
    seg = seg + 50
    if seg >= 60:
        seg = seg - 60
        min = min + 1
    if min >= 60:
        min = min - 60
        horas = horas + 1
    massa = massa / 2

print("Massa final:", massa)
print("Tempo:", horas, "h", min, "min", seg, "seg")