def conta_palavras(texto):
    palavras = texto.split()  
    contagem = {}  
    
    for palavra in palavras:
        
        palavra = palavra.lower()
        
    
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem


print(conta_palavras("banana maçã banana laranja maçã banana"))  


print(conta_palavras("O sol brilha forte o sol brilha no céu"))  


print(conta_palavras("Python é uma linguagem de programação"))  


print(conta_palavras("Olá Olá Olá"))  

