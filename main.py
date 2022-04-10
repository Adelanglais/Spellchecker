from DictionnaryLibrary import dictionnary_to_list
from DistanceLibrary import closests_words
from TF_IDF import computeTFIDF, getLemmes, getTokens
from TreeTaggerLibrary import analyserFichier
from TypingErrorsLibrary import existing_words
import numpy as np
import argparse


def parser_arguments():
    """
    Manage the input from the terminal.
    :return : parser
    """
    parser = argparse.ArgumentParser(prog = 'Correcteur_ToolKit',
                                    usage = 'python3 %(prog)s [command] --text [option] --corpus [option]',
                                    description='Ce programme permet de corriger les erreurs d\'un text par rapport à un corpus de référence')
    parser.add_argument("command",
                        metavar= "<command>: 'main'",
                        help = "'main'.")
    parser.add_argument('--text', required=False, nargs='+',
                    metavar="filename",
                    help="Sequence of 'strings' of the wanted text")
    parser.add_argument('--corpus', required=False, type=int, default=None,
                    metavar="corpus name",
                    help="Sequence of 'strings' of the wanted corpus")

    args = parser.parse_args()
    return args

if __name__ == "__main__":


    filename = 'text.txt' #parser_arguments().text
    corpus = 'corpus_test' #parser_arguments().corpus
    dictionnary = 'dictionnaire.txt'

    """
    Tokenisation et lemmatisation du texte fournit en entrée
    """
    file_tokens = getTokens(filename)
    file_lemmes = getLemmes(filename)
    
    #print("Tokens : ",file_tokens)
    
    """
    Génération d'une liste des corrections orthographique basées sur les fautes de frappes
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

    #print("Liste 1 erreurs fautes de frappes : ", L1, end='\n\n')
    
    """
    Génération d'une liste des corrections orthographique basées sur la distance lexicographique
    Quand la suggestion de correction est égale au mot tapé, on ne la prend pas en compte dans la liste finale
    
    Liste de listes : 
    chaque sous-liste correspond à un token
    le premier élément de la sous-liste est le token
    le deuxième élément de la sous-liste est la liste des corrections possibles du token
    """

    L2 = []
    for i in range(len(file_tokens)):
        dl_errors_liste = []
        correction = closests_words(file_tokens[i],dictionnary)
        if (len(correction) == 1 and correction[0] == file_tokens[i]):
            pass
        else:
            dl_errors_liste.append(file_tokens[i]) 
            dl_errors_liste.append(correction)
            L2.append(dl_errors_liste)

    #print("Liste 2 erreurs distance lexicographique : ", L2, end='\n\n')

    """
    Calcul de TF-IDF du text fournit en entrée 
    Plus cette valeur est élevée, plus le mot est rare --> il faut le corriger en premier
    """
    tfidf = computeTFIDF(filename,corpus)
    
    #print("TF-IDF : ", tfidf, end='\n\n')

    """
    Tri de L1 par TF-IDF
    On veut que les mots dont la valeur de TF-IDF est la plus élevée soit corrigés en premier
    """
    for liste in L1:
        for key, val in tfidf.items():
            if ( liste[0] == key):
                liste.append(val)
    
    L1 = sorted(L1,key = lambda x:x[2],reverse = True)
    
    #print("Liste triée par ordre décroissant : ", L1, end='\n\n')

    """
    Tri de L2 par TF-IDF
    On veut que les mots dont la valeur de TF-IDF est la plus élevée soit corrigés en premier
    """
    for liste in L2:
        for key, val in tfidf.items():
            if ( liste[0] == key):
                liste.append(val)
    
    L2 = sorted(L2,key = lambda x:x[2],reverse = True)
    
    #print("Liste triée par ordre décroissant : ", L2, end='\n\n')



