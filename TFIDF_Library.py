from prometheus_client import Counter
from TreeTaggerLibrary import *
import math 
from os import listdir
from os.path import isfile, join
from collections import Counter


def getLemmes (file):

    """ Accès aux lemmes des mots du fichier à traiter

    Paramètres
    ----------
    file : le fichier à analyser

    Returns 
    -------
    list 
        la liste des lemmes du fichier

    """

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    lemmes = []

    for i in range(len(liste_analyse)):
        
        # suppression des ponctuations, numéros, conjonctions de coordination, etc. car non pertinents pour l'analyse
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN' or liste_analyse[i][1] == 'KON' or liste_analyse[i][1] == 'DET' or liste_analyse[i][1] == 'PRP' or liste_analyse[i][1] == 'PRO'):
            pass

        else:

            # gestion des termes avec une sous-catégorie grammaticale
            if(len(liste_analyse[i]) > 3):
                lemmes.append((liste_analyse[i][3]).lower()) # récupération des lemmes
            
            else :
                lemmes.append((liste_analyse[i][2]).lower()) # récupération des lemmes
    
    return lemmes

# Affichage des lemmes du fichier
#print('Lemmes : ', getLemmes('mail.txt'))

def getTokens (file):

    """ Accès aux tokens des mots du fichier à traiter

    Paramètres
    ----------
    file : le fichier à analyser

    Returns 
    -------
    list 
        la liste des tokens du fichier

    """

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    tokens = []

    for i in range(len(liste_analyse)):
        
        # suppression des ponctuation, des pronoms, des déterminants, des conjonctions, etc. car non pertinents pour l'analyse 
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN' or liste_analyse[i][1] == 'KON' or liste_analyse[i][1] == 'DET' or liste_analyse[i][1] == 'PRP' or liste_analyse[i][1] == 'PRO'):
            pass

        else:
            tokens.append((liste_analyse[i][0]).lower())
    
    return tokens

# Affichage des tokens du fichier
#print ('Tokens : ', getTokens('mail.txt'))

def computeTF(file):

    """ Calcul de l'indicateur TF

    Fonction permet d'obtenir la fréquence des termes présents dans le document passé en paramètre

    Paramètres
    ----------
    file : le fichier à analyser

    Returns 
    -------
    dict 
        un dictionnaire --> à chaque tokens du texte est associé sa fréquence dans le document

    """

    tokens_liste = getTokens(file) # récupération des tokens du fichier texte
    wordsCount = len(tokens_liste) # récupération du nombre total de mots dans le fichier
    tfDict = Counter() # initialisation du dictionnaire
    
    for i in range(len(tokens_liste)):

        c = tokens_liste.count(tokens_liste[i]) # calcul du nombre de fois que le mot apparaît dans le texte
        tfDict[tokens_liste[i]] = c / float(len(tokens_liste)) # calcul de la fréquence et ajout au dictionnaire
        
    return tfDict

# Affichage de TF
#print("TF : ",computeTF('mail.txt'))

# Calcul de IDF - Donne la fréquence de documents du corpus contenant le terme T
def computeIDF(corpus):

    """ Calcul de l'indicateur IDF

    Fonction permettant de calculer la fréquence des documents du corpus contenant le terme T. 
    Cet indicateur permet de mettre en avant les mots saillants. 

    Paramètres
    ----------
    corpus : le corpus de textes à analyser

    Returns 
    -------
    dict 
        un dictionnaire --> à chaque tokens des textes du corpus est associé sa valeur d'IDF
            
    """
    
    fichiers = [f for f in listdir(corpus) if isfile(join(corpus, f))]
    N = len(fichiers) # récupération du nombre de documents présents dans le corpus

    tokens_liste = [] # initialisation de la liste des tokens du fichier traité
    
    # Création de la liste des tokens pour chaque textes présents dans le corpus
    for nom_document in fichiers :

        filename = corpus + "/" + nom_document
        tokens = getTokens(filename)
        tokens_liste.append(tokens) # tokens_liste contient une sous-liste de tokens pour chaque fichier du corpus
    
    idfCnt = Counter() # initialisation du dictionnaire d'IDF
  
    word_liste = [] # récupération de l'ensembe des tokens du corpus
    
    for i in range(len(tokens_liste)): # parcours de chaque liste de tokens des fichiers du corpus
        for j in range(len(tokens_liste[i])): # parcours de chaque tokens de le sous-liste
            word_liste.append(tokens_liste[i][j]) # ajout de ce token à word_liste
    
    word_liste = set(word_liste) # suppression des doublons --> word_liste contient tous les tokens du corpus
    
    # Calcul du nombre de textes dans lequel chacun des tokens du corpus apparaît
    for check_word in word_liste:
        for list in tokens_liste:
            for word in list:
                if word == check_word : 
                    idfCnt[word] += 1
                    break

    # Calcul d'IDF
    for key, val in idfCnt.items():
        idfCnt[key] = math.log(N/float(val))
      
    return idfCnt   

# Affichage d'IDF
#print("IDF : ",computeIDF('corpus_mail'))

def computeTFIDF(file, corpus):

    """ Calcul du score TF-IDf de l'ensemble des textes du corpus

    Paramètres
    ----------
    file : le fichier texte à corriger
    corpus : le corpus de textes à analyser

    Returns 
    -------
    dict 
        un dictionnaire --> à chaque tokens du texte à corriger est associé sa valeur de TF-IDF
    
    """
    
    tfidf = Counter()
    TF_liste = []

    fichiers = [f for f in listdir(corpus) if isfile(join(corpus, f))]
    N = len(fichiers)

    TF = computeTF(file) # fréquence du mot dans le text
    IDF = computeIDF(corpus) # rareté du mot dans le corpus de référence
   
    for keyTF, valTF in TF.items():
        
        for keyIDF, valIDF in IDF.items():    
            if keyTF == keyIDF:
                tfidf[keyTF] = valTF * valIDF # multiplication de l'indicateur TF par l'indicateur IDF

        if IDF.get(keyTF) == None : # cas où le mot traité n'est pas présent dans le corpus de text --> soit le mot est rare, soit le mot est mal orthographié
            tfidf[keyTF] = valTF*10
            
    return tfidf

# Affichage des résultats
#print(computeTFIDF('mail.txt','corpus_mail'))