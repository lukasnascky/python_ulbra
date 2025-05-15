#1
def identifica_sinal_bool(valor1):
    if valor1 >= 0:
        return True
    else:
        return False
    
#2
def identifica_sinal(valor1):
    if valor1 >= 0:
        return f"O valor {valor1} é positivo!"
    else:
        return f"O valor {valor1} é negativo!"
    
#3 
def valor_par_impar(valor1):
    if valor1 % 2 == 0:
        return f"O valor {valor1} é par!"
    else:
        return f"O valor {valor1} é impar!"
     
#4
def media_notas(nota1, nota2, nota3, tipo_media): #tipo media == A ou P
    if tipo_media == "A":
        media = (nota1 + nota2 + nota3) / 3
    elif tipo_media == "P":
        media = ((nota1 * 5) + (nota2 * 3) + nota3 * 2) / 10
    return media

#5
def idade_em_dias(anos, meses, dias):
    idade = (anos * 360) + (meses * 30) + dias
    return idade

#6
def ordenar_valores(a, b, c):
    if a < b and a < c:
        if b < c:
            return f"{str(a)}, {str(b)}, {str(c)}"
        else:
            return f"{str(a)}, {str(c)}, {str(b)}"
    elif b < a and b < c:
        if a < c:
            return f"{str(b)}, {str(a)}, {str(c)}"
        else:
            return f"{str(b)}, {str(c)}, {str(a)}"
    else:
        if a < b:
            return f"{str(c)}, {str(a)}, {str(b)}"
        else:
            return f"{str(c)}, {str(b)}, {str(a)}"

#7
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


#8
def verifica_num_perfeito(num):
    divisores = 0
    i = 1
    while i < num:
        if num % i == 0:
            divisores = divisores + i
        i = i + 1
    if num == divisores:
        return True
    else:
        return False

#9
def calcula_peso_ideal(alt, sexo):
    if sexo == "m":
        peso_ideal = (72.7 * alt) - 58
    elif sexo == "f":
        peso_ideal = (62.1 * alt) - 44.7
    return peso_ideal

#10
def verifica_triangulo(x, y, z):
    if (x < y + z) or (y < x + z) or (z < x + y): 
        if (x == y) and (y == z):
            return f"\nTriângulo Equilátero."
        elif (x != y) and (y != z):
            return f"\nTriângulo Escaleno."
        else:
            return f"\nTriângulo Isósceles."
    else:
        return f"\nNão é um triângulo!"