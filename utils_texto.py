def inverter_texto(texto):
    return texto[::-1]

def contar_vogais(texto):
    return sum(1 for c in texto.lower() if c in "aeiouáéíóúàèìòùâêîôû")

def eh_palindromo(texto):
    return texto.lower() == texto.lower()[::-1]