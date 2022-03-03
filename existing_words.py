from possible_words import possible_words
from dictionnary_to_list import dictionnary_to_list
import numpy as np

def existing_words(word, dictionnary):

    dictionnary_list = np.array(dictionnary_to_list(dictionnary))
    words_list = np.array(possible_words(word))
    
    final_liste = np.intersect1d(words_list,dictionnary_list)
    
    # Résultat
    return final_liste

# Test d'affichage du résultat
# print(existing_words('mzis','listemots.txt'))