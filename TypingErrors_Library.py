import numpy as np
from Dictionary_Library import dictionary_to_list


def letter_next_to (letter) :
    
    """ Fonction de correction d'un caractère en un caractère voisin

    Paramètres
    ----------
    letter : la lettre tapée

    Returns
    -------
    list
        liste des caractères voisins à la lettre tapée
        (clavier AZERTY) 

    """

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

def two_lists_merging(list1, list2):
    final_list = []
    for element1 in list1:
        for element2 in list2:
            final_list.append(element1+element2)
    return final_list


def possible_words(word) :

    """ Ensemble des corrections du mot possibles

    Paramètres
    ----------
    word : mot étudié

    Returns
    -------
    list
        une liste contenant toutes les combinaison de corrections des caractères qui composent le mot étudié
    """

    word = word.upper()
    
    # taille du mot passé en entrée
    n = len(word)

    # création de la liste des fautes possibles pour chaque lettre du mot 
    list_char = []
    for letter in word :
        list_char.append(letter_next_to(letter))
    
    n = len(list_char)
    words_list = list_char[0]
    count = 1

    while count != n:
        words_list = two_lists_merging(words_list,list_char[count])
        count += 1
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].lower()

    # Résultat
    return words_list

# Test d'affichage du résultat
# print(possible_words('mzis'))

def existing_words(word, dictionary):

    """ Filtrage des corrections 

    Fonctions permettant de ne garder que les combinaisons de caractères présentes dans le dictionnaire

    Paramètres
    ----------
    word : le mot à analyser
    dictionary : le dictionnaire

    Returns
    -------
    list 
        la liste des corrections du mot qui existent dans le dictionnaire    
    """

    # importation du dictionnaire sous forme de liste
    dictionary_list = np.array(dictionary_to_list(dictionary))

    # liste des combinaisons possibles
    words_list = np.array(possible_words(word))
    
    # comparaison des deux listes 
    liste = np.intersect1d(words_list,dictionary_list)

    final_liste = []
    for word in liste:
        final_liste.append(word)

    # Résultat
    return final_liste

# Test d'affichage du résultat
#print(existing_words('mzis','dictionnaire.txt'))

