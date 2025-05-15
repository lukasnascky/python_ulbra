tradutor = {"hello": "olá", "kiss": "beijo", "sugar": "açucar", "car": "carro"}

while True:
    palavra = input("\nEntrada: ")

    if palavra in tradutor:
        print(f"Saída: {tradutor[palavra]}")
    else:
        print("Palavra não encontrada!")