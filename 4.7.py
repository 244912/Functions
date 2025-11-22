###
# ICAO phonetic alphabet – zamienia litery na słowa
#
def icao_word(letter):
    words = {
        'A': 'Alpha',    'B': 'Bravo',    'C': 'Charlie',
        'D': 'Delta',    'E': 'Echo',     'F': 'Foxtrot',
        'G': 'Golf',     'H': 'Hotel',    'I': 'India',
        'J': 'Juliett',  'K': 'Kilo',     'L': 'Lima',
        'M': 'Mike',     'N': 'November', 'O': 'Oscar',
        'P': 'Papa',     'Q': 'Quebec',   'R': 'Romeo',
        'S': 'Sierra',   'T': 'Tango',    'U': 'Uniform',
        'V': 'Victor',   'W': 'Whiskey',  'X': 'Xray',
        'Y': 'Yankee',   'Z': 'Zulu'
    }
    return words.get(letter.upper(), '?')

name = input("Wpisz imię: ")

spelled = []

for letter in name:
    if letter.isalpha():  
        word = icao_word(letter)
        spelled.append(word)

print("Twoje imię w alfabecie ICAO:")
print(" ".join(spelled))