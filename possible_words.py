from numpy import append
from letter_next_to import letter_next_to

def two_lists_merging(list1, list2):
    final_list = []
    for element1 in list1:
        for element2 in list2:
            final_list.append(element1+element2)
    return final_list

def possible_words(word) :

    word = word.upper()

    # taille du mot passé en entrée
    n = len(word)

    # création de la liste des fautes possibles pour chaque lettre du mot 
    list_char = []
    for letter in word :
        list_char.append(letter_next_to(letter))
    
    n = len(list_char)
    words_list = list_char[0]
    count = 1

    while count != n:
        words_list = two_lists_merging(words_list,list_char[count])
        count += 1
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].lower()

    # Résultat
    return words_list

# Test d'affichage du résultat
# print(possible_words('mzis'))



