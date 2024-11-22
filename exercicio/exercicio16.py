def conta_vogais(texto):
    vogais = "aeiouAEIOU"  
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


print(conta_vogais("Python"))        
print(conta_vogais("Programação"))   
print(conta_vogais("AEIOU"))         
print(conta_vogais("bcdfg"))         
print(conta_vogais("Olá, mundo!"))   
