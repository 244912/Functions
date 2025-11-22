# Funkcja sprawdza, czy kiedykolwiek w pokoju były co najmniej 3 osoby jednocześnie
def f(detector):
    osoby = 0          
    max_osoby = 0      

    for znak in detector:
        if znak == '+':
            osoby = osoby + 1
        elif znak == '-':
            osoby = osoby - 1
        
        # sprawdzamy po każdym ruchu
        if osoby > max_osoby:
            max_osoby = osoby

    # jeżeli maksymalnie było 3 lub więcej → True
    return max_osoby >= 3