# Funkcja rekurencyjnie oblicza sumę liczb od 1 do n
def sum_natural(n):
    # Jeśli n = 1 → suma to 1
    if n == 1:
        return 1
    
    # W przeciwnym razie: n + suma od 1 do (n-1)
    return n + sum_natural(n - 1)