def lista_pares(numeros):

    return [numero for numero in numeros if numero % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Os números pares na lista são: {lista_pares(numeros)}")
