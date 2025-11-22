import range_check

liczba = int(input("A number: "))
zakres_od = 2
zakres_do = 15

czy_w_zakresie = range_check.is_in_range(liczba, zakres_od, zakres_do)

print(f"Number {liczba} in the range <{zakres_od},{zakres_do}>: {'yes' if czy_w_zakresie else 'no'}")