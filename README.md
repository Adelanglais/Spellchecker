# Spellchecker

## Général

### *Objectif du programme :*
Ce code permet en une seule ligne de commande, de corriger un fichier texte passé en paramètre. Ce fichier sera corrigé par rapport à un corpus de référence.

## Installation

* fonctionne avec python3
* nécessite l'installation de *TreeTagger*

### **1. Cloner le projet git dans votre répertoire de travail**

```python
git clone https://github.com/Adelanglais/Spellchecker
```

### **2. Gestion du corpus et du texte à corriger**
Dans le répertoire du projet se trouvent les éléments suivants :  

* *corpus_mail* : un dossier contenant des mails de référence
* *test_mail.txt* : un fichier texte contenant le mail que nous souhaitons corriger

Ces deux éléments sont modifiables selon ce que vous souhaitez corriger. D'autre corpus peuvent être ajoutés dans des dossiers spécifiques : il vous suffira de préciser lequel vous souhaitez utiliser lorsque vous lancerez le programme dans le terminal. 

## Utilisation

*Exemple d'utilisation du programme*

```python
python main.py doCorrections --text mail.txt --corpus corpus_mail
```

## Liste des commandes 

1. *getOriginalText* : pour visualiser le texte original avant corrections

```python
python main.py getOriginalText --text [exemple]
```

1. *compareTexts* : pour visualiser le texte original avant corrections et celui corrigé

```python
python main.py compareTexts --text [exemple]
```

**Arguments**

1. *--text* : attend le nom du fichier à corriger
2. *--corpus* : attend le nom du dossier corpus

## Fonctionnement général du programme 

