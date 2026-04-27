from utils_texto import inverter_texto, contar_vogais, eh_palindromo

def test_inverter_texto():
    assert inverter_texto("ola") == "alo"

def test_inverter_vazio():
    assert inverter_texto("") == ""

def test_contar_vogais():
    assert contar_vogais("hello") == 2

def test_contar_vogais_maiusculas():
    assert contar_vogais("AEIOU") == 5

def test_eh_palindromo_verdadeiro():
    assert eh_palindromo("arara") == True

def test_eh_palindromo_falso():
    assert eh_palindromo("hello") == False