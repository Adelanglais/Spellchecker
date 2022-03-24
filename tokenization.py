def tokanization(file):
    
    """ Fonction de tokenisation 
    
    Cette fonction permet de segmenter un texte

    Paramètres 
    -----------
    file : fichier txt 

    Returns
    -------
    list
        une liste contenant les tokens du texte

    Règles de segmentation 
    -----------------------
    - suppression des ponctions --> . , ! ? / () % # : 
    - cas de l'appostrophe --> séparation du mot en deux, l'appostrophe est conservée avec le mot à gauche
    - cas du trait d'union --> pas de découpage
    """ 
    
    # initialisation de la liste des tokens du texte passé en paramètres
    tokens= []    
    # liste des ponctuations à supprimer dans le texte
    ponctuation = ['.',',',':','?','!','(',')','/','#','=','%']
    
    with open(file, 'r') as f :
        string = f.read()
        for char in string:
            # suppression de la ponctuation
            for i in ponctuation : 
                if (char==i) :
                    string = string.replace(char, "")
                if (char=='\n') :
                    string = string.replace(char, " ")
            if (char == "'" ):
                string = string.replace(char,char + " ")

        # découpage du texte à chaque espace
        word = string.split(' ')
        # ajout des tokens à la liste
        tokens.extend(word)

    # suppression des éléments vides et des espaces présents dans la liste
    while " " in tokens:
         del tokens[tokens.index(' ')]
    while "" in tokens:
         del tokens[tokens.index('')]

    # Résultat  
    return tokens

# test affichage des résultats
# print(tokanization('text.txt'))