def numeros_primos_ate(n):

    if n < 2:
        return []  

    primos = []
    for num in range(2, n + 1):
        is_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    
    return primos


n = 30
print(f"Os números primos até {n} são: {numeros_primos_ate(n)}")
