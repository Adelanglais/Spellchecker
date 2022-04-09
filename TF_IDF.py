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
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN'):
            pass
        else:
            # gestion des termes avec une sous-catégorie grammaticale
            if(len(liste_analyse[i])>3):
                # récupération des lemmes
                lemmes.append(liste_analyse[i][3])
            else :
                lemmes.append(liste_analyse[i][2])
    
    return lemmes

def getTokens (file):

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    tokens = []
    for i in range(len(liste_analyse)):
        # suppression des ponctuation et des numéros car non pertinents pour l'analyse des 
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN'):
            pass
        else:
            # gestion des termes avec une sous-catégorie grammaticale
            if(len(liste_analyse[i])>3):
                # récupération des lemmes
                tokens.append(liste_analyse[i][3])
            else :
                tokens.append(liste_analyse[i][2])
    
    return tokens

# Calcul de TF - Donne la fréquence d'un terme dans un document
def computeTF(file):
    lemmes_liste = getLemmes(file)
    wordsCount = len(lemmes_liste)
    tfDict = {}
    
    for i in range(len(lemmes_liste)):
        c = lemmes_liste.count(lemmes_liste[i])
        tfDict[lemmes_liste[i]] = c / float(len(lemmes_liste))
    
    return tfDict

 
# Calcul de IDF - Donne la fréquence de documents du corpus contenant le terme T
def computeIDF(corpus):
    
    fichiers = [f for f in listdir(corpus) if isfile(join(corpus, f))]
    N = len(fichiers)
    lemmes_liste = []
    idfDict = {}
    
    for nom_document in fichiers :

        filename = corpus + "/" + nom_document
        lemmes = getLemmes(filename)
        lemmes_liste.append(lemmes)
    
    idfCnt = Counter()
  
    word_liste = []
    for i in range(len(lemmes_liste)):
        for j in range(len(lemmes_liste[i])):
            word_liste.append(lemmes_liste[i][j])
    word_liste = set(word_liste)
    
    #print(lemmes_liste)
    for check_word in word_liste:
        for list in lemmes_liste:
            for word in list:
                if word == check_word : 
                    idfCnt[word] += 1
                    break
             
    for key, val in idfCnt.items():
        idfCnt[key] = math.log(N/float(val))
    #print(idfCnt)
    
    return idfCnt     


# Calcul du score TF-IDf de l'ensemble des textes du corpus
def computeTFIDF(file, corpus):
    
    tfidf = Counter()
    TF_liste = []

    TF = computeTF(file) # fréquence du mot dans le text
    IDF = computeIDF(corpus) # rareté du mot dans le corpus de référence

    print(TF)
    print(IDF)

    for keyTF, valTF in TF.items():
        for keyIDF, valIDF in IDF.items():
            if(keyTF == keyIDF):
                tfidf[keyTF] = valTF * valIDF
            
            #Gestion du cas où le mot testé n'est pas présent dans le corpus de référence ??? 
                      
    return tfidf

# Affichage des résultats
# computeTFIDF('text.txt','corpus_test')