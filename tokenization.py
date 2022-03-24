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
    
    tokens= []    
    ponctuation = ['.',',',':','?','!','(',')','/','#','=','%']
    
    with open(file, 'r') as f :
        string = f.read()
        for char in string:
            for i in ponctuation : 
                if (char==i) :
                    string = string.replace(char, "")
                if (char=='\n') :
                    string = string.replace(char, " ")
            if (char == "'" ):
                string = string.replace(char,char + " ")
        
        word = string.split(' ')
        tokens.extend(word)

    while " " in tokens:
         del tokens[tokens.index(' ')]
    while "" in tokens:
         del tokens[tokens.index('')]

    # Résultat  
    return tokens

# test affichage des résultats
# print(tokanization('text.txt'))