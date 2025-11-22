def power(x, n):
    # Jeśli potęga jest 0 → każda liczba do potęgi 0 = 1
    if n == 0:
        return 1
    
    # W przeciwnym razie: x^n = x * x^(n-1)
    return x * power(x, n - 1)