# Funkcja tworzy akronim z pierwszych liter słów
def f(name):
    slowa = name.split()       # dzieli tekst na słowa (po spacji)
    akronim = ""
    
    for slowo in slowa:
        akronim = akronim + slowo[0].upper()   # bierze pierwszą literę i dużą
    
    return akronim