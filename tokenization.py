def tokanization(file):
    
    tokens= []    
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
        tokens.extend(word)

    while " " in tokens:
         del tokens[tokens.index(' ')]
    while "" in tokens:
         del tokens[tokens.index('')]

    # Résultat  
    return tokens

# test affichage des résultats
#print(tokanization('text.txt'))