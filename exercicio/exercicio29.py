def substituir_vogais(texto, caractere):

    vogais = 'aeiouAEIOU'
    nova_string = ''.join([caractere if char in vogais else char for char in texto])
    return nova_string

texto = "Vamo vamo vamo Botafogo"
caractere = "*"
print(f"Texto original: {texto}")
print(f"Texto modificado: {substituir_vogais(texto, caractere)}")

