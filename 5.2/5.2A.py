# converters.py
# Ten plik zawiera funkcje do przeliczania długości

def cm_to_m(cm):
    """
    Zamienia centymetry na metry.
    1 m = 100 cm → więc dzielimy przez 100.
    """
    return cm / 100


def m_to_cm(m):
    """
    Zamienia metry na centymetry.
    1 m = 100 cm → więc mnożymy przez 100.
    """
    return m * 100


# NOWA FUNKCJA 1: cm → cale
def cm_to_inches(cm):
    """
    Zamienia centymetry na cale.
    1 cal = 2.54 cm → więc dzielimy cm przez 2.54
    Przykład: 10 cm → 10 / 2.54 ≈ 3.94 cala
    """
    return cm / 2.54


# NOWA FUNKCJA 2: stopy i cale → centymetry
def feet_inches_to_cm(stopy, cale=0):
    """
    Zamienia stopy (i opcjonalnie cale) na centymetry.
    1 stopa = 12 cali
    1 cal = 2.54 cm

    Przykład:
    - 5 stóp 0 cali → 5 * 12 = 60 cali → 60 * 2.54 = 152.4 cm
    - 5 stóp 9 cali → (5*12 + 9) = 69 cali → 69 * 2.54 ≈ 175.26 cm
    """
    wszystkie_cale = stopy * 12 + cale   # najpierw zamień stopy na cale
    centymetry = wszystkie_cale * 2.54   # potem cale na cm
    return centymetry