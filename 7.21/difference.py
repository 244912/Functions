# Funkcja zwraca różnicę między największą a najmniejszą z trzech liczb
def f(number1, number2, number3):
    najwieksza = max(number1, number2, number3)
    najmniejsza = min(number1, number2, number3)
    return najwieksza - najmniejsza