from dictionnary_to_list import dictionnary_to_list

def add_word_to_dictionnary(word,file) :
    """ Ajouter un mot au dictionnaire

    Paramètres 
    -----------
    word : le mot que l'on veut ajouter au dictionnaire
    file : le dictionnaire 

    """

    dictionnary=dictionnary_to_list(file)

    if (word.lower() not in dictionnary) :
        fichier = open(file, "a")
        # écriture du mot dans le fichier 
        fichier.write('\n'+ word.lower())
        fichier.close() 
      
    return 

# Test d'affichage du résultat
# add_word_to_dictionnary('BOUBliboulga','listemots.txt')
# print(dictionnary_to_list('listemots.txt'))

