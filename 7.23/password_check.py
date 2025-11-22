#Funkcja sprawdza, czy hasło jest poprawne (min. 6 znaków i wszystkie różne)
def f(password):
    # Jeśli hasło ma mniej niż 6 znaków → False
    if len(password) < 6:
        return False
    
    # Sprawdzamy, czy wszystkie znaki są różne
    for i in range(len(password)):
        for j in range(i + 1, len(password)):
            if password[i] == password[j]:
                return False
    
    # Jeśli wszystko OK → True
    return True