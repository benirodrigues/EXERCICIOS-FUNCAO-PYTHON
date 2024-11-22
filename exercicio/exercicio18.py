def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


print(ordenar_lista([5, 3, 8, 6, 2]))   
print(ordenar_lista([1, 2, 3, 4, 5]))    
print(ordenar_lista([9, 7, 5, 3, 1]))    
print(ordenar_lista([]))                
print(ordenar_lista([10]))               
