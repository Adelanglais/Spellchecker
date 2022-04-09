def dictionnary_to_list(file) :
    
    """ Importation du dictionnaire sous forme d'une liste de mots

    Paramètres 
    -----------
    file : le dictionnaire

    Returns
    -------
    list
        une liste contenant l'ensemble des mots du dictionnaire

    """

    final_list = []
    with open(file, 'r') as f :
        lignes = f.readlines()
        for ligne in lignes :
            final_list.append((ligne.strip('\n')).lower())
    
    # Résultat
    return final_list

# Test d'affichage du résultat
# print(dictionnary_to_list('listemots.txt'))

def add_word_to_dictionnary(word,file) :

    """ Ajout d'un mot au dictionnaire

    Paramètres 
    -----------
    word : le mot que l'on veut ajouter au dictionnaire
    file : le dictionnaire 

    """

    dictionnary = dictionnary_to_list(file)

    if (word.lower() not in dictionnary) :
        fichier = open(file, "a")
        # écriture du mot dans le fichier 
        fichier.write('\n'+ word.lower())
        fichier.close() 
      
    return 

