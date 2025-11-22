def dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        pierwsze_dwa = 2 * 10.5
        reszta = (human_years - 2) * 4
        return pierwsze_dwa + reszta