def f(dice):
    if len(dice) == 0:      # jeśli pusty tekst
        return 0
    
    max_seria = 1           # najdłuższa seria (na początek 1)
    aktualna_seria = 1      # obecna seria
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:     # jeśli taka sama cyfra jak poprzednia
            aktualna_seria = aktualna_seria + 1
        else:
            # kończy się seria – sprawdzamy czy była dłuższa
            if aktualna_seria > max_seria:
                max_seria = aktualna_seria
            aktualna_seria = 1       # zaczynamy nową serię
    
    # po pętli sprawdzamy ostatnią serię
    if aktualna_seria > max_seria:
        max_seria = aktualna_seria
    
    return max_seria