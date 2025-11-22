def hide(card_number):
    widoczne_poczatek = card_number[0:2]      
    widoczne_koniec = card_number[-4:]        
    gwiazdki = "*" * 10                       
    return widoczne_poczatek + gwiazdki + widoczne_koniec