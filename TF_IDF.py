from ast import arguments
from matplotlib.pyplot import text
from maLibrairieTreeTagger import *
import math 
import argparse
import sys

from os import listdir
from os.path import isfile, join

def getLemmes (file):

    # récupération de la liste des tokens + lemmes (analyse morphosyntaxique)
    liste_analyse = analyserFichier(file)

    lemmes = []
    for i in range(len(liste_analyse)):
        # suppression des ponctuation et des numéros car non pertinents pour l'analyse des 
        if (liste_analyse[i][1] == 'SENT' or liste_analyse[i][1] == 'PUN' or liste_analyse[i][1] == 'NUM'):
            pass
        else:
            # gestion des termes avec une sous-catégorie grammaticale
            if(len(liste_analyse[i])>3):
                # récupération des lemmes
                lemmes.append(liste_analyse[i][3])
            else :
                lemmes.append(liste_analyse[i][2])
    
    return lemmes
    #print(lemmes)

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
    idfDict = {}

    for i in range(N):
        lemmes_liste = getLemmes(fichiers[i])

    




computeIDF('Baudelaire')

