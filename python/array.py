# Lista de números
listas = [-44,0, 185, 2, 3, 4, 55, 6, 7, 8, 9, 14561]

# Ordena a lista numericamente
listas.sort()  
# Analisa e imprime os números na lista ordenada
for lista in listas:
    if lista == 0:
        print(lista, "nulo")
    elif lista < 0:
        print(lista,"numero negativo")
    elif lista % 2 == 0:
        print(lista, "par")
    else:
        print(lista, "ímpar")

print(listas)



    
     





#print("minha lista na posição",x,":",lista [x])

#mudar valor da posição 3:
#lista[3] = 100
#print("minha lista modificada:", lista)

#adcionar um valor a mais no array:
#lista.append(11)
#print("minha lista com valor adcionado:", lista)

#delete o valor da posição 2
#del lista[2]
#print("posição 2 deletada:", lista)
#print (n)