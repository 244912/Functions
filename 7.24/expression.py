# Funkcja oblicza wynik prostego dodawania i odejmowania (tylko cyfry)
def f(expression):
    wynik = 0
    liczba = 0
    
    for znak in expression:
        if znak == "+":           # jeśli + → dodajemy kolejną liczbę
            continue
        elif znak == "-":         # jeśli - → odejmujemy kolejną liczbę
            continue
        else:
            # to jest cyfra
            cyfra = int(znak)
            if znak == expression[0]:     # pierwsza liczba zawsze jest dodawana
                wynik = cyfra
            else:
                # patrzymy na poprzedni znak
                poprzedni = expression[expression.index(znak)-1]
                if poprzedni == "+":
                    wynik = wynik + cyfra
                elif poprzedni == "-":
                    wynik = wynik - cyfra
    
    return wynik