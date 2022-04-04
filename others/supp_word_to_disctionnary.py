from dictionnary_to_list import dictionnary_to_list


def supp_word_to_dictionnary(word,file) :

    dictionnary=dictionnary_to_list(file)
    word=word.lower()
    if (word in dictionnary) :
        dictionnary.remove(word)

        fichier = open(file, "w")
        for w in dictionnary :
            fichier.write('\n'+ w)
        fichier.close() 
      
    return 

#Test et affichage
# supp_word_to_dictionnary('BOUBliboulga','listemots.txt')
# print(dictionnary_to_list('listemots.txt'))