# Funkcja zwraca n-tą liczbę ciągu Fibonacciego
def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    a = 0   # pierwsza liczba
    b = 1   # druga liczba
    
    for i in range(3, n+1):
        c = a + b   # nowa liczba = suma dwóch poprzednich
        a = b       # przesuwamy
        b = c       # przesuwamy
    
    return b