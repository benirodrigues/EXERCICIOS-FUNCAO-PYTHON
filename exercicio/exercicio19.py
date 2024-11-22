def eh_palindromo(texto):
    
    texto_limpo = ''.join(texto.lower().split())
    
    return texto_limpo == texto_limpo[::-1]


print(eh_palindromo("Apos a sopa"))       
print(eh_palindromo("A base do teto desaba"))  
print(eh_palindromo("Python"))           
print(eh_palindromo("arara"))           
print(eh_palindromo("12321"))            
print(eh_palindromo("12345"))            
