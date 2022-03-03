
def letter_next_to (letter) :
    
    # Fonction de correction d'un caractère en un caractère voisin

    list_nextCharacter = []
    
    if letter == 'A':
        list_nextCharacter = ['Q','Z','A']    
    if letter == 'B':
        list_nextCharacter = ['B','V','G','H','N']
    if letter == 'C':
        list_nextCharacter = ['C','X','D','F','V']
    if letter == 'D':
        list_nextCharacter = ['D','E','R','F','C','X','S']
    if letter == 'E':
        list_nextCharacter = ['E','Z','S','D','R']
    if letter == 'F':
        list_nextCharacter = ['F','D','R','T','G','V','C']
    if letter == 'G':
        list_nextCharacter = ['G','F','T','Y','H','B','V']
    if letter == 'H':
        list_nextCharacter = ['H','G','Y','U','J','N','B']
    if letter == 'I':
        list_nextCharacter = ['I','U','J','K','O']
    if letter == 'J':
        list_nextCharacter = ['J','H','U','I','K','N']
    if letter == 'K':
        list_nextCharacter = ['K','J','I','O','L']
    if letter == 'L':
        list_nextCharacter = ['L','K','O','P','M']
    if letter == 'M':
        list_nextCharacter = ['M','L','P']
    if letter == 'N':
        list_nextCharacter = ['N','B','H','J']
    if letter == 'O':
        list_nextCharacter = ['O','I','K','L','P']
    if letter == 'P':
        list_nextCharacter = ['P','O','L','M']
    if letter == 'Q':
        list_nextCharacter = ['Q','A','Z','S','W']
    if letter == 'R':
        list_nextCharacter = ['R','D','F','T']
    if letter == 'S':
        list_nextCharacter = ['S','Q','Z','E','D','X','W']
    if letter == 'T':
        list_nextCharacter = ['T','R','F','G','Y']
    if letter == 'U':
        list_nextCharacter = ['U','Y','H','J','I']
    if letter == 'V':
        list_nextCharacter = ['V','C','F','G','B']
    if letter == 'W':
        list_nextCharacter = ['W','Q','S','X']
    if letter == 'X':
        list_nextCharacter = ['X','W','S','D','C']
    if letter == 'Y':
        list_nextCharacter = ['Y','T','G','H','U']
    if letter == 'Z':
        list_nextCharacter = ['Z','A','Q','S','E']
    else :
        None
    
    # Résultat
    return list_nextCharacter

# Test d'affichage du résultat    
#print(nextCharacter('A'))