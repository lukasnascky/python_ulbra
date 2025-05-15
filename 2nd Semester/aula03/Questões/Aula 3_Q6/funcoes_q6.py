def encontra_animal(chave1, chave2, chave3):
    if chave1 == "vertebrado":
        if chave2 == "ave":
            if chave3 == "carnivoro":
                return f"Águia"
            elif chave3 == "onivoro":
                return f"Pomba"
            
        elif chave2 == "mamifero":
            if chave3 == "onivoro":
                return f"Homem"
            elif chave3 == "herbivoro":
                return f"Vaca"
            
    elif chave1 == "invertebrado":
        if chave2 == "inseto":
            if chave3 == "hematofago":
                return f"Pulga"
            elif chave3 == "herbivoro":
                return f"Lagarta"
            
        if chave2 == "anelideo":
            if chave3 == "hematofago":
                return f"Sanguessuga"
            elif chave3 == "onivoro":
                return f"Minhoca"
            
    return f"Não encontrado!"
#_#