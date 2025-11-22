def sum_digits(number):
    number = abs(number)
    
    suma = 0
    
    for cyfra in str(number):
        suma = suma + int(cyfra)
    
    return suma

x = int(input("Podaj liczbę: "))

print("Suma cyfr liczby", x, "to:", sum_digits(x))