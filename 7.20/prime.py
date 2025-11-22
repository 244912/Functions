# Funkcja zwraca n-tą liczbę pierwszą
def f(n):
    if n == 1:
        return 2
    
    liczba = 3          # zaczynamy od pierwszej nieparzystej liczby po 2
    znalezione = 1      # już mamy jedną liczbę pierwszą (czyli 2)
    
    while znalezione < n:
        # sprawdzamy, czy liczba jest pierwsza
        jest_pierwsza = True
        
        for i in range(3, liczba, 2):  # sprawdzamy tylko nieparzyste dzielniki
            if i * i > liczba:         # nie musimy sprawdzać dalej niż sqrt(liczba)
                break
            if liczba % i == 0:
                jest_pierwsza = False
                break
        
        if jest_pierwsza:
            znalezione = znalezione + 1
            if znalezione == n:
                return liczba
        
        liczba = liczba + 2    # następna nieparzysta liczba