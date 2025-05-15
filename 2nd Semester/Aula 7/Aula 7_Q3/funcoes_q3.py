def verifica_comiss(vendas):
    comiss = 200 + vendas * 0.09

    if comiss < 300:
        return "a"
    
    elif comiss < 400:
        return "b"
    
    elif comiss < 500:
        return "c"
    
    elif comiss < 600:
        return "d"
    
    elif comiss < 700:
        return "e"
    
    elif comiss < 800:
        return "f"
    
    elif comiss < 900:
        return "g"
    
    elif comiss < 1000:
        return "h"
    
    return "i"