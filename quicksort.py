lista = [10, 7, 8, 9, 1, 5 , 140 , 44 , 59 , 77 , 81 , 2]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        left = [x for x in lista[1:] if x <= pivot]  
        right = [x for x in lista[1:] if x > pivot]  
        
        return quick_sort(left) + [pivot] + quick_sort(right)


print(f"\nLista desordenada:",(lista),"\nLista ordenada:   ", quick_sort(lista))


