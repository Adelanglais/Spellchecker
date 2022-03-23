def tokanization(file):
    
    final_list = []    
    ponctuation = ['.',',',':','?','!','(',')','/','#',]
    
    with open(file, 'r') as f :
        string = f.read()
        for char in string:
            for i in ponctuation : 
                if (char==i) :
                    string = string.replace(char, "")
                if (char=='\n') :
                    string = string.replace(char, " ")
            if (char == "'" ):
                string = string.replace(char,char + " ")
        
        word = string.split(' ')
        final_list.extend(word)

    while " " in final_list:
         del final_list[final_list.index(' ')]
    while "" in final_list:
         del final_list[final_list.index('')]

    # Résultat  
    return final_list

# test affichage des résultats
#print(tokanization('text.txt'))