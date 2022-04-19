import textdistance
from Dictionary_Library import dictionary_to_list

def closests_words(word, dictionary):

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
    list_dictionary = dictionary_to_list(dictionary) # passage du dictionnaire sous format list
    closests_words = [] # initialisation de la liste

    for j in list_dictionary : 

        # pour chaque mot du dictionnaire, on calcule la distance avec le mot du passé en paramètre
        distance = textdistance.levenshtein(word,j)

        # si cette distance est inférieur à un certain seuil, nous ajoutons le mot du dictionnaire à notre liste
        # remarque : la valeur de seuil est fixée arbitrairement --> plus elle est élevée, plus y aura de mots possibles dans notre liste
        if len(word) <= 6: 
            if distance <= 1 :
                closests_words.append(j)
        
        if len(word) > 6 :
            if distance <= 2 :
                closests_words.append(j)

    
    # Résultat
    return closests_words

# Test affichage des résultats
#print(closests_words('infromatique','dictionnaire.txt'))
