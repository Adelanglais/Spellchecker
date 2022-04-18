from encodings import utf_8
from DictionnaryLibrary import add_word_to_dictionnary, dictionnary_to_list
from DistanceLibrary import closests_words
from TF_IDF import computeIDF, computeTFIDF, getLemmes, getTokens
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

def n_repl(s, sub, repl, n):

    longueur = len(sub)
    compteur = 1
    find = s.find(sub) # = indice de la 1ere iteration
    avant = s[:find]
    apres = s[(find+longueur):]

    while compteur < n:

        find = apres.find(sub)
        avant = avant + sub + apres[:find]
        apres = apres[(find+longueur):]
        compteur += 1

    return avant + repl + apres

def printText(filename):

    fichier = open(filename,'r',encoding= 'utf-8')
    print(fichier.read())

if parser_arguments().command == 'getOriginalText':

        if parser_arguments().text is None:
            print("Missing text argument")
            exit(1)
        
        else : 
            printText(parser_arguments().text[0])

""" if parser_arguments().command == 'compareTexts':

        if parser_arguments().text is None:
            print("Missing text argument")
            exit(1)

        else : 
            print("\nORIGINAL TEXT :")
            print("---------------")
            printText(parser_arguments().text[0])

            print("\nCORRECTED TEXT :")
            print("------------------")
            printText(parser_arguments().text[1]) """

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
        printText(parser_arguments().text[0])

        filename = parser_arguments().text[0]
        corpus = parser_arguments().corpus[0]
        dictionnary = 'dictionnaire.txt'

        """
        Tokenisation et lemmatisation du texte fournit en entrée
        """
        file_tokens = list(set(getTokens(filename)))
        file_lemmes = list(set(getLemmes(filename)))
        
        #print(file_tokens)
        #print(file_lemmes)

        """
        L1 et L2 - Création des listes de fautes de frappes
        """
        L1 = [] # liste des erreurs frappes
        L2 = [] # liste basé sur le calcul de distance lexicographique

        for token in file_tokens:
            
            typing_errors_liste = []
            dl_errors_liste = []
            correction_typing = []
            token = token.lower()

            if len(token) <= 7:
                correction_typing = existing_words(token,dictionnary)
            else:
                correction_typing = []

            correction_dl = closests_words(token,dictionnary)
            
            if (len(correction_typing) == 1 and correction_typing[0] == token):
                pass
            elif len(correction_typing)==0 :
                pass
            else:
                typing_errors_liste.append(token) 
                typing_errors_liste.append(correction_typing)
                L1.append(typing_errors_liste)

            if (len(correction_dl) == 1 and correction_dl[0] == token):
                pass
            elif len(correction_dl)==0 :
                pass
            else:
                dl_errors_liste.append(token) 
                dl_errors_liste.append(correction_dl)
                L2.append(dl_errors_liste)
            
        #print("L1 : ", L1)
        #print("L2 : ",L2)

        """
        L3 - Combinaison des listes L1 et L2
        Objectif : n'avoir qu'une seule liste regroupant l'ensemble des corrections possibles quelque soit l'origine de la faute
        """   
        
        L1 = np.array(L1, dtype=object)
        L2 = np.array(L2, dtype=object)

        tokens_L1 = L1[:,0]
        tokens_L2 = L2[:,0]

        words_L1 = L1[:,1]
        words_L2 = L2[:,1]

        L3 = []

        for index_L1,token_L1 in enumerate(tokens_L1):

            if token_L1 in tokens_L2:
                index_L2 = int(np.where(tokens_L2 == token_L1)[0])
                token_L2 = tokens_L2[index_L2]
                liste_mots_combines = list(np.unique(np.concatenate((words_L1[index_L1],words_L2[index_L2]),0)))
                L3.append( [token_L1, liste_mots_combines] )
            else:
                L3.append( list(L1[index_L1,:]) )


        for index_L2,token_L2 in enumerate(tokens_L2):

            if not token_L2 in tokens_L1: L3.append( list(L2[index_L2,:]) )
        
        #print("L3.1 : ",L3)
      
        """
        TF-IDF
        """
        tfidf = computeTFIDF(filename,corpus)

        """
        Tri des corrections possibles pour chaque mots - on ne garde que celles qui sont les plus probables
        """

        """ idf = computeIDF(corpus) # calcul de l'importance des mots dans le corpus

        for i in range(len(L3)):

            corrections = L3[i][1]
            new = []

            for word in corrections:
                
                # Traitement du cas où la correction n'est pas présente dans le corpus
                # Toutes les corrections sont gardées
                
                if word not in idf.keys():
                    new.append(word)

                # Si la correction est dans le corpus et que sa valeur d'IDF est supérieure à un certain seuil, on garde 
                # la correction
                # Sinon, la correction n'est pas conservée car non pertinente par rapport au corpus   
                for key, val in idf.items():
                    if word == key and val > 1 : 
                        new.append(word)
            
            L3[i][1] = new
        
        print("L3.2 : ",L3) """
        
        """
        Tri de la liste des corrections - Priorisation des mots les plus saillants
        """
        
        for liste in L3:
            for key, val in tfidf.items():
                if ( liste[0] == key):
                    liste.append(val)
        
        L3 = sorted(L3,key = lambda x:x[2],reverse = True)
                        
        """
        Gestion du fichier de correction
        """
        
        with open(filename, 'r+', encoding= 'utf-8') as firstfile, open('correctedText.txt','a') as secondfile:
            secondfile.truncate(0)          # on supprimer tout ce qu'il y a écrit dans le fichier
            for line in firstfile :
                secondfile.write(line) # on recopie le premier fichier dans le fichier retour de correction
        
        with open(filename,'r', encoding='utf-8') as file :
            x = file.read().lower()
            x = x.replace('\'',' ')
            x = x.replace(',',' ')
            x = x.replace('.',' ')
            x = x.replace('\n',' ')
            words = x.split()

        print("\nCORRECTEUR D\'ORTHOGRAPHE :")
        print("--------------------------------")
        print("Tapez l'indice de la correction que vous souhaitez effectuer.")
        print("Revoir  -->  ['debout', 'devoir', 'revoir'] : pour changer 'revoir' en 'debout', tapez 1.")
        print("Pour ajouter le mot au dictionnaire, tapez +.")
        print("Pour ne rien faire, tapez -.")
        print("--------------------------------\n")

        for liste in L3 :
            
            counter = words.count(liste[0])
            
            for occurence in range(counter):

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
                    
                    if (j == -1):
                        print("Choix incorrect")
                    
                    else:
                        print ("'",liste[0],"'", " sera remplacé par '", liste[1][j], "' dans le texte.")

                        with open('correctedText.txt','r') as file :
                            x = file.read()
                            x = n_repl(x, liste[0], liste[1][j], 1)
                        
                        with open('correctedText.txt','w') as file :
                            file.truncate(0)
                            file.write(x)
        

        print("\nFICHIER AVEC CORRECTION :")
        print("----------------------------")
        fichier = open('correctedText.txt','r')
        print(fichier.read(),'\n\n')
