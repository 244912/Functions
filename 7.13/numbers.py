# Funkcja łączy liczby od 1 do n w jeden tekst
def f(n):
    tekst = ""
    for i in range(1, n+1):
        tekst = tekst + str(i)
    return tekst