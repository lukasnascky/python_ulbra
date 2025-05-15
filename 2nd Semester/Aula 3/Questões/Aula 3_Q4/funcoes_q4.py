def verifica_pode_votar(idade, nacionalidade):
    if idade > 15 and (nacionalidade == "brasileiro" or nacionalidade == "brasileira"):
        return f"Pode votar!"
    else:
        return f"Não pode votar!"

def verifica_categoria(idade):
    if idade < 0:
        return f"Idade inválida!"
    elif idade <= 11:
        return f"Criança"
    elif idade <= 20:
        return f"Adolescente"
    elif idade <= 30:
        return f"Jovem"
    elif idade <= 59:
        return f"Adulto"
    elif idade >= 60:
        return f"Idoso"
    
def verifica_alistamento(idade, sexo):
    if sexo == "m":
        if idade > 17:
            return f"Deve se alistar!"
        else:
            return f"Ainda não precisa se alistar!"
    else:
        return f"Não pode se alistar!"
#_#