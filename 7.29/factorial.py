# Funkcja oblicza silnię rekurencyjnie (n! = n × (n-1) × ... × 1)
def factorial(n):
    # 0! = 1 i 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Dla większych liczb: n! = n × (n-1)!
    if n > 1:
        return n * factorial(n - 1)