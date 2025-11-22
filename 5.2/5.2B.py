# test_converters.py
# Ten plik testuje wszystkie funkcje z converters.py

import converters  # ładujemy funkcje z innego pliku

def main():
    print("=== TESTUJEMY PRZELICZNIKI ===")
    print()

    # 1. Test starej funkcji: cm → m
    print("1. Centymetry na metry:")
    print(f"   150 cm → {converters.cm_to_m(150)} m")
    print(f"   250 cm → {converters.cm_to_m(250)} m")
    print()

    # 2. Test starej funkcji: m → cm
    print("2. Metry na centymetry:")
    print(f"   1.5 m → {converters.m_to_cm(1.5)} cm")
    print(f"   3 m → {converters.m_to_cm(3)} cm")
    print()

    # 3. NOWA FUNKCJA: cm → cale
    print("3. Centymetry na cale:")
    print(f"   10 cm  → {converters.cm_to_inches(10):.2f} cala")
    print(f"   25.4 cm → {converters.cm_to_inches(25.4):.2f} cala")  # to powinno dać 10.00
    print(f"   100 cm → {converters.cm_to_inches(100):.2f} cala")
    print()

    # 4. NOWA FUNKCJA: stopy + cale → cm
    print("4. Stopy i cale na centymetry:")
    print(f"   5 stóp 0 cali → {converters.feet_inches_to_cm(5, 0):.1f} cm")
    print(f"   5 stóp 9 cali → {converters.feet_inches_to_cm(5, 9):.1f} cm")
    print(f"   6 stóp 2 cale → {converters.feet_inches_to_cm(6, 2):.1f} cm")
    print(f"   Tylko 12 cali → {converters.feet_inches_to_cm(0, 12):.1f} cm")  # 0 stóp, 12 cali

# Uruchom program, jeśli plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()