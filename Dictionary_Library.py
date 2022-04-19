def dictionary_to_list(file) :
    
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
    
    with open(file, 'r',encoding='UTF-8') as f :
        lignes = f.readlines()
        for ligne in lignes :
            final_list.append((ligne.strip('\n')).lower())
    
    # Résultat
    return final_list

# Test d'affichage du résultat du dictionnaire
# print(dictionary_to_list('dictionnaire.txt'))

def add_word_to_dictionary(word,file) :

    """ Ajout d'un mot au dictionnaire

    Paramètres 
    -----------
    word : le mot que l'on veut ajouter au dictionnaire
    file : le dictionnaire 

    """

    dictionary = dictionary_to_list(file)

    if (word.lower() not in dictionary) :
        fichier = open(file, "a",encoding='UTF-8')
        
        # écriture du mot dans le fichier 
        fichier.write('\n'+ word.lower())
        fichier.close() 
      
    return 

