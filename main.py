"""
@author: Alix DE LANGLAIS <alix.delanglais@edu.esiee.fr>
@author: Lisa SERAIRI <lisa.serari@edu.esiee.fr
"""

from DictionnaryLibrary import dictionnary_to_list
from DistanceLibrary import closests_words
from TF_IDF import computeTFIDF, getLemmes, getTokens
from TreeTaggerLibrary import analyserFichier
from TypingErrorsLibrary import existing_words
import numpy as np



if __name__ == "__main__":

    filename = 'text.txt'
    corpus = 'corpus_test'
    dictionnary = 'dictionnaire.txt'

    """
    Tokenisation et lemmatisation du texte fournit en entrée
    """
    file_tokens = getTokens(filename)
    file_lemmes = getLemmes(filename)
    print("Tokens : ",file_tokens)
    
    """
    Génération d'un dictionnaire des corrections orthographique basées sur les fautes de frappes
    Quand la suggestion de correction est égale au mot tapé, on ne la prend pas en compte dans la liste finale
    
    Liste de listes : 
    chaque sous-liste correspond à un token
    le premier élément de la sous-liste est le token
    le deuxième élément de la sous-liste est la liste des corrections possibles du token
    """
    
    L1 = []
    for i in range(len(file_tokens)):
        typing_errors_liste = []
        correction = existing_words(file_tokens[i],dictionnary)
        if (len(correction) == 1 and correction[0] == file_tokens[i]):
            pass
        else:
            typing_errors_liste.append(file_tokens[i]) 
            typing_errors_liste.append(correction)
            L1.append(typing_errors_liste)

    print("Liste erreurs fautes de frappes : ", L1)
    
    """
    Génération d'un dictionnaire des corrections orthographique basées sur la distance lexicographique
    key : le token
    value : liste des corrections possibles
    """
    #distance_errors_dict = {}
    #for i in range(len(file_tokens)):
    #    distance_errors_dict[file_tokens[i]] = closests_words(file_tokens[i],dictionnary)
    
    #print("Erreurs distance lexicographique : ", distance_errors_dict)

    """
    Calcul de TF-IDF du text fournit en entrée 
    Plus cette valeur est élevée, plus le mot est rare --> il faut le corriger en premier
    """
    tfidf = computeTFIDF(filename,corpus)
    print("TF-IDF : ", tfidf)

    """
    Tri de L1 par TF-IDF
    On veut que les mots dont la valeur de TF-IDF est la plus élevée soit corrigés en premier
    """
    for liste in L1:
        for key, val in tfidf.items():
            if ( liste[0] == key):
                liste.append(val)
    
    print("Ajout valeur TF-IDF : ", L1)


    print("Liste triée par ordre décroissant : ", L1)

    

    
    # Tri de L2 par TF-IDF  



    # Passage du dictionnaire au format liste
    dictionnaire_liste = dictionnary_to_list('dictionnaire.txt')

