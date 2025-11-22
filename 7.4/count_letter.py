def count_letter(text, letter):
    ile = 0
    for znak in text:
        if znak == letter:
            ile = ile + 1
    return ile