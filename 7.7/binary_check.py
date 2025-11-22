def f(binary_number):
    for znak in binary_number:
        if znak != '0' and znak != '1':
            return False
    return True