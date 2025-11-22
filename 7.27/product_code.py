def f(product_code):
    # Kod musi mieć dokładnie 4 znaki
    if len(product_code) != 4:
        return False
    
    # Bierzemy pierwsze 3 cyfry
    pierwsze_trzy = product_code[0:3]
    kontrolna = product_code[3]   # czwarta cyfra
    
    # Zamieniamy na liczby
    cyfra1 = int(pierwsze_trzy[0])
    cyfra2 = int(pierwsze_trzy[1])
    cyfra3 = int(pierwsze_trzy[2])
    cyfra_kontrolna = int(kontrolna)
    
    # Obliczamy sumę pierwszych trzech cyfr
    suma = cyfra1 + cyfra2 + cyfra3
    
    # Obliczamy resztę z dzielenia przez 7
    reszta = suma % 7
    
    # Sprawdzamy, czy cyfra kontrolna się zgadza
    return reszta == cyfra_kontrolna