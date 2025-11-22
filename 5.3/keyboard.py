def input_string(message):
    tekst = input(message)
    return tekst

def input_integer(message):
    liczba = int(input(message))
    return liczba

def input_real(message):
    liczba = float(input(message))
    return liczba

def input_boolean(message):
    odpowiedz = input(message).lower()
    if odpowiedz == 'y':
        return True
    else:
        return False