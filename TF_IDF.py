from matplotlib.pyplot import text
from prometheus_client import Counter
from TreeTaggerLibrary import *
import math 
from os import listdir
from os.path import isfile, join
from collections import Counter


def getLemmes (file):

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    lemmes = []
    for i in range(len(liste_analyse)):
        # suppression des ponctuation et des numéros car non pertinents pour l'analyse des 
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN' or liste_analyse[i][1] == 'KON' or liste_analyse[i][1] == 'DET' or liste_analyse[i][1] == 'PRP'):

            pass
        else:
            # gestion des termes avec une sous-catégorie grammaticale
            if(len(liste_analyse[i])>3):
                # récupération des lemmes
                lemmes.append((liste_analyse[i][3]).lower())
            else :
                lemmes.append((liste_analyse[i][2]).lower())
    
    return lemmes


def getTokens (file):

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    tokens = []
    for i in range(len(liste_analyse)):
        # suppression des ponctuation, des pronoms, des déterminants et des conjonctions car non pertinents pour l'analyse 
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN' or liste_analyse[i][1] == 'KON' or liste_analyse[i][1] == 'DET' or liste_analyse[i][1] == 'PRP'):
            pass
        else:
            tokens.append((liste_analyse[i][0]).lower())
    #print(tokens)
    return tokens

# Calcul de TF - Donne la fréquence d'un terme dans un document
def computeTF(file):
    tokens_liste = getTokens(file)
    wordsCount = len(tokens_liste)
    tfDict = Counter()
    
    for i in range(len(tokens_liste)):
        c = tokens_liste.count(tokens_liste[i])
        tfDict[tokens_liste[i]] = c / float(len(tokens_liste))
        
    return tfDict

#print(computeTF('text.txt'))

# Calcul de IDF - Donne la fréquence de documents du corpus contenant le terme T
def computeIDF(corpus):
    
    fichiers = [f for f in listdir(corpus) if isfile(join(corpus, f))]
    N = len(fichiers)
    tokens_liste = []
    idfDict = {}
    
    for nom_document in fichiers :

        filename = corpus + "/" + nom_document
        tokens = getTokens(filename)
        tokens_liste.append(tokens)
    
    idfCnt = Counter()
  
    word_liste = []
    for i in range(len(tokens_liste)):
        for j in range(len(tokens_liste[i])):
            word_liste.append(tokens_liste[i][j])
    word_liste = set(word_liste)
    
    #print(lemmes_liste)
    for check_word in word_liste:
        for list in tokens_liste:
            for word in list:
                if word == check_word : 
                    idfCnt[word] += 1
                    break
             
    for key, val in idfCnt.items():
        idfCnt[key] = math.log(N/float(val))
      
    return idfCnt   

#print(computeIDF('corpus_test'))

# Calcul du score TF-IDf de l'ensemble des textes du corpus
def computeTFIDF(file, corpus):
    
    tfidf = Counter()
    TF_liste = []

    fichiers = [f for f in listdir(corpus) if isfile(join(corpus, f))]
    N = len(fichiers)

    TF = computeTF(file) # fréquence du mot dans le text
    IDF = computeIDF(corpus) # rareté du mot dans le corpus de référence

    #print("TF : ",TF)
    #print("IDF : ",IDF)
    
    for keyTF, valTF in TF.items():
        for keyIDF, valIDF in IDF.items():
            
            if keyTF == keyIDF:
                tfidf[keyTF] = valTF * valIDF

        if IDF.get(keyTF)==None : # cas où le mot traité n'est pas présent dans le corpus de text --> soit le mot est rare, soit le mot est mal orthographié
            # tfidf[keyTF] = valTF * math.log(N)
            tfidf[keyTF] = valTF*10
            
    return tfidf

# Affichage des résultats
#print(computeTFIDF('text.txt','corpus_test'))