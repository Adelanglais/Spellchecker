import textdistance
from dictionnary_to_list import dictionnary_to_list
from existing_words import existing_words

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
        distance = textdistance.levenshtein(word,j)
        if distance <= 1 :
            closests_words.append(j)
    
    closests_words = set(closests_words)

    return closests_words

# test affichage des résultats
# print(closests_words('mzis','listemots.txt'))
