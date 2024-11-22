def area_circulo(raio):

    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    
    pi = 3.14  
    return pi * (raio ** 2)


raio = 5
print(f"A área do círculo com raio {raio} é {area_circulo(raio):.2f}")


