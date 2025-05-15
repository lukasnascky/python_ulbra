from funcoes import *

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
lista2 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

while True:
    menu = int(input('''
1. Count
2. Extend
3. Insert
4. Remove
5. Pop
6. Index
7. Sort
8. Reverse
9. Sair
>>>'''))
    
    if menu == 1:
        v_count = int(input("\nValor:"))
        print("Count =", l_count(lista1, v_count))

    elif menu == 2:
        print(l_extend(lista1, lista2))
    
    elif menu == 3:
        item = int(input("\nItem: "))
        posi = int(input("Posição: "))
        print(l_insert(lista1, posi, item))
    
    elif menu == 4:
        item = int(input("\nItem: "))
        print(l_remove(lista1, item))
    
    elif menu == 5:
        posi = int(input("\nPosição: "))
        print(l_pop(lista1, posi))
    
    elif menu == 6:
        item = int(input("\nItem: "))
        print(l_index(lista1, item))

    elif menu == 7:
        print("Lista1: ", l_sort(lista2))

    elif menu == 8:
        print("Lista1: ", l_reverse(lista1))
    
    elif menu == 9:
        break