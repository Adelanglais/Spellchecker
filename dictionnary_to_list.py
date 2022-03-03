import readline

def dictionnary_to_list(file) :
    final_list = []
    with open(file, 'r') as f :
        lignes = f.readlines()
        for ligne in lignes :
            final_list.append(ligne.strip('\n'))
    # Résultat
    return final_list

# Test d'affichage du résultat
# print(dictionnary_to_list('listemots.txt'))