import dog_age

lata_ludzkie = int(input("Enter the dog's age in human years: "))
lata_psie = dog_age.dog_years(lata_ludzkie)

print(f"The dog's age in dog's years is {int(lata_psie)} years.")