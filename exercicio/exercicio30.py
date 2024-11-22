def juntar_listas(lista1, lista2):

    return list(set(lista1 + lista2))


lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print(f"Lista combinada sem duplicatas: {juntar_listas(lista1, lista2)}")
