import numpy as np
from sympy import li
from dictionnary_to_list import dictionnary_to_list
from existing_words import existing_words

def levenshtein_distance(chaine1,chaine2):
    """
    La distance de Levenshtein est une mesure permettant d'évaluer la distance entre deux chaînes de caractère.
    Elle se calcul avec la détermination du nombre minimum de caractère à modifier pour transformer la chaîne en une autre. 
    Il faut calculer la distance entre deux lettres à la même position dans les deux chaînes.
    
    Paramètres
    ----------
    chaine1 : mot 1 à comparer
    chaine2 : mot 2 à comparer

    Returns
    -------
    int
        la distance entre les deux chaînes passées en paramètres 

    """
    taille_chaine1 = len(chaine1) + 1
    taille_chaine2 = len(chaine2) + 1
    levenshtein_matrix = np.zeros ((taille_chaine1, taille_chaine2))
    for x in range(taille_chaine1):
        levenshtein_matrix [x, 0] = x
    for y in range(taille_chaine2):
        levenshtein_matrix [0, y] = y

    for x in range(1, taille_chaine1):
        for y in range(1, taille_chaine2):
            if chaine1[x-1] == chaine2[y-1]:
                levenshtein_matrix [x,y] = min(
                    levenshtein_matrix[x-1, y] + 1,
                    levenshtein_matrix[x-1, y-1],
                    levenshtein_matrix[x, y-1] + 1
                )
            else:
                levenshtein_matrix [x,y] = min(
                    levenshtein_matrix[x-1,y] + 1,
                    levenshtein_matrix[x-1,y-1] + 1,
                    levenshtein_matrix[x,y-1] + 1
                )
    distance = levenshtein_matrix[taille_chaine1 - 1, taille_chaine2 - 1]

    return (distance)

def closests_words(word, dictionnary):

    """Calcul de la distance Lexicographique

    Cette fonction calcule la distance de Levenshtein entre un mot
    présenté en entrée et chacun des mots composant le dictionnaire

    Paramètres
    ----------
    word : le mot à analyser
    dictionnaire : le dictionnaire

    Returns 
    -------
    list 
        la liste des mots du dictionnaire dont la distance avec le mot
        est inférieure à certain seuil
    
    """

    word = word.lower()
    list_dictionnary = dictionnary_to_list(dictionnary)
    closests_words = []

    for j in list_dictionnary : 
        distance = levenshtein_distance(word,j)
        if distance <= 1 :
            closests_words.append(j)
    
    closests_words = set(closests_words)

    return closests_words

# test affichage des résultats
# print(closests_words('mzis','listemots.txt'))
