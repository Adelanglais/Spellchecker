from DictionnaryLibrary import add_word_to_dictionnary, dictionnary_to_list
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
                        metavar= "<command>: 'getOriginalText', 'doCorrections' or 'compareTexts'.",
                        help = "'getOriginalText', 'doCorrections' or 'compareTexts'.")
    parser.add_argument('--text', required=False, nargs='+',
                    metavar="filename",
                    help="Sequence of 'strings' of the wanted text")
    parser.add_argument('--corpus', required=False, nargs='+',
                    metavar="corpus name",
                    help="Sequence of 'strings' of the wanted corpus")

    args = parser.parse_args()
    return args

def printOriginalText(filename):
    fichier = open(filename,'r')
    print(fichier.read())

if parser_arguments().command == 'getOriginalText':
        if parser_arguments().text is None:
            print("Missing text argument")
            exit(1)
        else : 
            printOriginalText(parser_arguments().text[0])

if parser_arguments().command == 'doCorrections':
    if parser_arguments().text is None:
        print("Missing text argument")            
        exit(1)
    if parser_arguments().corpus is None:
        print("Missing corpus argument")
        exit(1)
    
if __name__ == "__main__":

    if parser_arguments().command == 'doCorrections':
        
        print("\nORIGINAL TEXT :")
        print("---------------")
        printOriginalText(parser_arguments().text[0])

        filename = parser_arguments().text[0]
        corpus = parser_arguments().corpus[0]
        dictionnary = 'dictionnaire.txt'

        """
        Tokenisation et lemmatisation du texte fournit en entrée
        """
        file_tokens = getTokens(filename)
        #file_lemmes = getLemmes(filename)

        """
        L1 - Liste des fautes de frappes
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

        """
        L2 - Liste des distances lexicographiques
        """
        """L2 = []
        for i in range(len(file_tokens)):
            dl_errors_liste = []
            correction = closests_words(file_tokens[i],dictionnary)
            if (len(correction) == 1 and correction[0] == file_tokens[i]):
                pass
            else:
                dl_errors_liste.append(file_tokens[i]) 
                dl_errors_liste.append(correction)
                L2.append(dl_errors_liste)"""
        
        """
        TF-IDF
        """
        tfidf = computeTFIDF(filename,corpus)

        """
        Tri de L1 et L2 par TF-IDF
        """
        for liste in L1:
            for key, val in tfidf.items():
                if ( liste[0] == key):
                    liste.append(val)
        L1 = sorted(L1,key = lambda x:x[2],reverse = True)

        """for liste in L2:
            for key, val in tfidf.items():
                if ( liste[0] == key):
                    liste.append(val)
        L2 = sorted(L2,key = lambda x:x[2],reverse = True)"""

        with open(filename, 'r+') as firstfile, open('correctedText.txt','a') as secondfile:
            secondfile.truncate(0)          # on supprimer tout ce qu'il y a écrit dans le fichier
            for line in firstfile :
                secondfile.write(line) # on recopie le premier fichier dans le fichier retour de correction

        print("\nCORRCTIONS - FAUTES DE FRAPPES :")
        print("--------------------------------")
        print("Tapez l'indice de la correction que vous souhaitez effectuer.")
        print("Revoir  -->  ['debout', 'devoir', 'revoir'] : pour changer 'revoir' en 'debout', tapez 1.")
        print("Pour ajouter le mot au dictionnaire, tapez +.")
        print("Pour ne rien faire, tapez -.")
        print("--------------------------------\n")
        
        for liste in L1 :
            
            print ("Suggestions de corrections pour : ", liste[0], " --> ", liste[1])
            
            j = input("Choisissez le mot (tapez l'indice - début à 1) : ")           

            if str(j) == '+':
                print("Ajout de '",liste[0],"' au dictionnaire.")
                #add_word_to_dictionnary(liste[0],dictionnary)
            
            elif str(j)== '-':
                pass
            
            else:
                
                j = int(j) -1 
                
                if (j >= (len(liste[1]))):
                    print("Choix incorrect") 

                else:
                    print ("'",liste[0],"'", " sera remplacé par '", liste[1][j], "' dans le texte.")

                    with open('correctedText.txt','r') as file :
                        x = file.read()
                        x = x.replace(liste[0],liste[1][j])
                    
                    with open('correctedText.txt','w') as file :
                        file.write(x)
        
        print("\nCORRCTIONS - DISTANCE LEXICOGRAPHIQUE :")
        print("--------------------------------")
        print("Tapez l'indice de la correction que vous souhaitez effectuer.")
        print("Revoir  -->  ['debout', 'devoir', 'revoir'] : pour changer 'revoir' en 'debout', tapez 1.")
        print("Pour ajouter le mot au dictionnaire, tapez +.")
        print("Pour ne rien faire, tapez -.")
        print("--------------------------------\n")

        """
        for liste in L2 :
            
            print ("Suggestions de corrections pour : ", liste[0], " --> ", liste[1])
            
            j = input("Choisissez le mot (tapez l'indice - début à 1) : ")

            j = int(j) -1 
        
            if (j > (len(liste[1]))):
                print("Choix incorrect") 

            else:
                print (liste[0], " sera remplacé par ", liste[1][j], " dans le texte.")

                with open('correctedText.txt','r') as file :
                    x = file.read()
                    x = x.replace(liste[0],liste[1][j])
                
                with open('correctedText.txt','w') as file :
                    file.write(x)
        """

        print("\nFICHIER AVEC CORRECTION :")
        print("----------------------------")
        fichier = open('correctedText.txt','r')
        print(fichier.read(),'\n\n')