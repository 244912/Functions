# Funkcja sprawdza, czy tekst jest palindromem (czyta się tak samo od tyłu)
def f(tekst):
    czysty = ""
    for znak in tekst:
        if znak.isalnum():          # tylko litery i cyfry
            czysty = czysty + znak.lower()
    
    # Sprawdzamy, czy czysty tekst czyta się tak samo od tyłu
    return czysty == czysty[::-1]