# Funkcja wstawia myślnik między wszystkie znaki w tekście
def f(text):
    wynik = ""                # pusty tekst na początek
    
    for i in range(len(text)):
        if i > 0:            # od drugiej litery dodajemy myślnik
            wynik = wynik + "-"
        wynik = wynik + text[i]   # dodajemy aktualną literę
    
    return wynik
