# Funkcja usuwa wszystkie spacje z tekstu
def f(sentence):
    bez_spacji = ""
    for znak in sentence:
        if znak != " ":
            bez_spacji = bez_spacji + znak
    return bez_spacji