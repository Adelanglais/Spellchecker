import textdistance
from Dictionnary_Library import dictionnary_to_list

def closests_words(word, dictionnary):

    """ Calcul de la distance Lexicographique

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

    word = word.lower() # suprresion des majuscules
    list_dictionnary = dictionnary_to_list(dictionnary) # passage du dictionnaire sous format list
    closests_words = [] # initialisation de la liste

    for j in list_dictionnary : 

        # pour chaque mot du dictionnaire, on calcule la distance avec le mot du passé en paramètre
        distance = textdistance.levenshtein(word,j)

        # si cette distance est inférieur à un certain seuil, nous ajoutons le mot du dictionnaire à notre liste
        # remarque : la valeur de seuil est fixée arbitrairement --> plus elle est élevée, plus y aura de mots possibles dans notre liste
        if distance <= 1 :
            closests_words.append(j)
    
    # Résultat
    return closests_words

# Test affichage des résultats
#print(closests_words('mzis','dictionnaire.txt'))