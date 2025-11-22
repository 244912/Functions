# Funkcja sumuje liczby z zakresu <x,y>, które są podzielne przez 2 i 3, ale NIE przez 4
def f(x, y):
    suma = 0
    for liczba in range(x, y):
        if liczba % 2 == 0 and liczba % 3 == 0 and liczba % 4 != 0:
            suma = suma + liczba
    return suma