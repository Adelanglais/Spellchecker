
def nextCharacter (character) :
    
    # Fonction de correction d'un caractère en un caractère voisin

    list_nextCharacter = []
    
    if character == 'A':
        list_nextCharacter = ['Q','Z','A']    
    if character == 'B':
        list_nextCharacter = ['B','V','G','H','N']
    if character == 'C':
        list_nextCharacter = ['C','X','D','F','V']
    if character == 'D':
        list_nextCharacter = ['D','E','R','F','C','X','S']
    if character == 'E':
        list_nextCharacter = ['E','Z','S','D','R']
    if character == 'F':
        list_nextCharacter = ['F','D','R','T','G','V','C']
    if character == 'G':
        list_nextCharacter = ['G','F','T','Y','H','B','V']
    if character == 'H':
        list_nextCharacter = ['H','G','Y','U','J','N','B']
    if character == 'I':
        list_nextCharacter = ['I','U','J','K','O']
    if character == 'J':
        list_nextCharacter = ['J','H','U','I','K','N']
    if character == 'K':
        list_nextCharacter = ['K','J','I','O','L']
    if character == 'L':
        list_nextCharacter = ['L','K','O','P','M']
    if character == 'M':
        list_nextCharacter = ['M','L','P']
    if character == 'N':
        list_nextCharacter = ['N','B','H','J']
    if character == 'O':
        list_nextCharacter = ['O','I','K','L','P']
    if character == 'P':
        list_nextCharacter = ['P','O','L','M']
    if character == 'Q':
        list_nextCharacter = ['Q','A','Z','S','W']
    if character == 'R':
        list_nextCharacter = ['R','D','F','T']
    if character == 'S':
        list_nextCharacter = ['S','Q','Z','E','D','X','W']
    if character == 'T':
        list_nextCharacter = ['T','R','F','G','Y']
    if character == 'U':
        list_nextCharacter = ['U','Y','H','J','I']
    if character == 'V':
        list_nextCharacter = ['V','C','F','G','B']
    if character == 'W':
        list_nextCharacter = ['W','Q','S','X']
    if character == 'X':
        list_nextCharacter = ['X','W','S','D','C']
    if character == 'Y':
        list_nextCharacter = ['Y','T','G','H','U']
    if character == 'Z':
        list_nextCharacter = ['Z','A','Q','S','E']
    
    return list_nextCharacter
    
