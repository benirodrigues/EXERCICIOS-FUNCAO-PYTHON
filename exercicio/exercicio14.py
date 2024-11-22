def fatorial(n):
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(fatorial(0))  
print(fatorial(1))  
print(fatorial(5))  
print(fatorial(7))  
