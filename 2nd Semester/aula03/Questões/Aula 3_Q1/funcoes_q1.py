def verifica_lucro(v_gasto, qtd_passageiros, v_recebido):
    lucro = (v_recebido * qtd_passageiros) - v_gasto
    
    if lucro > 0:
        return f"Houve Lucro!"
    elif lucro < 0:
        return f"Houve prejuizo!"
    else:
        return f"A viagem se pagou!"
    #_#