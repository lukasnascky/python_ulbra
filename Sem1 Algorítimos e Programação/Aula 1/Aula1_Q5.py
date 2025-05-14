clip_plastico = int(input("Caixas de clips de plástico vendidas: "))
clip_metal = int(input("Caixas de clips de metal vendidas: "))

total_plastico = clip_plastico * 5.0
total_metal = clip_metal * 10.0

print(f"\nValor arrecadado com clips de plático: R$ {total_plastico}")
print(f"Valor arrecadado com clips de metal: R$ {total_metal}")
print(f"Total arrecadado: R$ {total_plastico + total_metal}")