def buchstabe_ändern(string, buchstabe):
    string_lower = string.lower()
    
    for v in "aeiou": #v - Vokale
        new_sentence =  []
        
        for char in string_lower:  #char - Character
            if char == buchstabe: 
                new_sentence.append(v)
            else: 
                new_sentence.append(char)
                
        print("".join(new_sentence))
        
buchstabe_ändern("BANANA", "a")

buchstabe_ändern("wie geht es Ihnen?", "e")