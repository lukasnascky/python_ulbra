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

num = int(input("Digite um número: "))
print(verifica_num_perfeito(num))
#_#