from possible_words import possible_words
from dictionnary_to_list import dictionnary_to_list
import numpy as np

def existing_words(word, dictionnary):

    """Filtrage des corrections 

    Fonctions permettant de ne garder que les combinaisons de caractères
    présentes dans le dictionnaire

    Paramètres
    ----------
    word : le mot à analyser
    dictionnary : le dictionnaire

    Returns
    -------
    list 
        la liste des corrections du mot qui existent dans le dictionnaire
        
    
    """
    # importation du dictionnaire sous forme de liste
    dictionnary_list = np.array(dictionnary_to_list(dictionnary))
    # liste des combinaisons possibles
    words_list = np.array(possible_words(word))
    # comparaison des deux listes 
    final_liste = np.intersect1d(words_list,dictionnary_list)
    
    # Résultat
    return final_liste

# Test d'affichage du résultat
# print(existing_words('mzis','listemots.txt'))