def eh_primo(numero):
    if numero <= 1:
        return False  
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  
    return True  


print(eh_primo(2))   
print(eh_primo(4))  
print(eh_primo(13))  
print(eh_primo(1))   
print(eh_primo(0))   
