"""
Created on Sun Mar 21 06:33:58 2021

@author: Adrien UGON <adrien.ugon@esiee.fr>
"""

import treetaggerwrapper
import re

from regex import regex

#Exploitation des sorties de TreeTagger:
def getAnnotationsFromTreeTaggerTags(tags):
    annotations = []
    # On parcourt toutes les lignes
    for ligne in tags:
        champs = ligne.split("\t") # Les champs sont séparés par une tabulation
        if (len(champs)>=3):        
            token = champs[0].replace("\n","") # On récupère le token (premier champ retourné par Tree-Tagger)
            categories = champs[1].replace("\n","") # On récupère la catégorie grammaticle (deuxième champ retourné par Tree-Tagger)
            # TreeTagger retourne 2 informations dans la colonne catégories grammaticales : la catégorie et la sous-catégorie
            if ":" in categories:
                souscategories = categories.split(":") # On divise le champ en deux parties
                categorie = souscategories[0] # Catégorie principale
                souscategorie = souscategories[1] # Sous catégorie
            else:
                categorie = categories # Catégorie principale
                souscategorie = None # Il n'y a pas de sous catégorie
            lemme = champs[2].replace("\n","") # On récupère le lemme (troisième champ retourné par Tree-Tagger)
            annotation = (token, categorie, souscategorie, lemme) #  On place les informations dans un tuple
            annotations.append(annotation) # On ajoute le tuple à la liste des annotations
            
    return annotations

# Analyse morphosyntaxique
def analyseMorphoSyntaxiqueTexte(texte, langue='fr'):
    # On exécute Tree-Tagger
    tagger = treetaggerwrapper.TreeTagger(TAGLANG=langue)
    #2) tag your text.
    tags = tagger.tag_text(texte)
    
    return getAnnotationsFromTreeTaggerTags(tags)

def analyserFichier(filename):

    #Ouverture du fichier texte
    document_source = open(filename,"r",encoding='utf8')

    #Lecture du contenu du compte-rendu
    contenu = document_source.read()

    # Regex - Numéro de téléphone
    regex_num = '([\+])?((([\d]{2,3}( )?(.)?){4,5}([\d]{2}){1})|(\d{10}))'
    replace_num = '<NUMERO TELEPHONE>'

    # Regex - Adresse e-mail
    regex_mail = '[a-z\d_.%+-]+@[a-z\d.-]+\.[a-z]{2,4}'
    replace_mail = '<ADRESSE MAIL>'

    # Regex - Adresse Web
    regex_web = '(https(s)?://)?(www\.)?(?<!@)[\w\-\.]+(\.com|\.fr)(/[\w]*)*'
    replace_web = '<ADRESSE INTERNET>'

    # Liste des expressions régulières à chercher dans le texte
    liste_regex = [[regex_num,replace_num],[regex_mail,replace_mail],[regex_web,replace_web]]
    
    for i in range(len(liste_regex)):
        annotated_file = re.sub(liste_regex[i][0],liste_regex[i][1],contenu)
        contenu = annotated_file
    print(annotated_file)

    annotations = analyseMorphoSyntaxiqueTexte(annotated_file)
    
    word = []
    final_liste = []

    for annotation in annotations:
        if annotation[2]:
            word.append(annotation[0])
            word.append(annotation[1])
            word.append(annotation[2])
            word.append(annotation[3])
            #print("{}\t{}:{}\t{}" . format(annotation[0],annotation[1],annotation[2],annotation[3]))
        else:
            word.append(annotation[0])
            word.append(annotation[1])
            word.append(annotation[3])
            #print("{}\t{}\t\t{}" . format(annotation[0],annotation[1],annotation[3]))
        final_liste.append(word)
        word = []
    
    return final_liste

# Test d'affichage du résultat
analyserFichier("text.txt")
    