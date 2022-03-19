from dictionnary_to_list import dictionnary_to_list


def add_word_to_dictionnary(word,file) :

    dictionnary=dictionnary_to_list(file)

    if (word.lower() not in dictionnary) :
        fichier = open(file, "a")
        fichier.write('\n'+ word.lower())
        fichier.close() 
      
    return 


# Test d'affichage du résultat
# add_word_to_dictionnary('BOUBliboulga','listemots copy.txt')
# print(dictionnary_to_list('listemots copy.txt'))

