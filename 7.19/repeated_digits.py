def f(number):
    tekst = str(number)       # zamieniamy liczbę na tekst
    suma = 0
    
    # Sprawdzamy każdą cyfrę od 0 do 9
    for cyfra in range(10):
        ile_razy = tekst.count(str(cyfra))   # ile razy występuje
        
        if ile_razy > 1:         # jeśli więcej niż raz
            suma = suma + cyfra  # dodajemy tę cyfrę do sumy
    
    return suma