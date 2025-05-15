def segundos_para_tempo(seg):
    seg_restante = 0
    minutos = 0
    horas = 0
    if seg > 0:
        seg_restante = seg % 60
        minutos = int(seg / 60)
    if minutos > 0:
        horas = int(minutos / 60)
        minutos = minutos % 60
    return f"{horas}:{minutos}:{seg_restante}"

segundos = int(input("Segundos: "))
print(segundos_para_tempo(segundos))
#_#