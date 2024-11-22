def fibonacci(n):
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]  

    sequencia = [0, 1]  
    for _ in range(2, n):
        proximo = sequencia[-1] + sequencia[-2]  
        sequencia.append(proximo)
    return sequencia


print(fibonacci(0))  
print(fibonacci(1))  
print(fibonacci(2))  
print(fibonacci(5))  
print(fibonacci(10)) 
