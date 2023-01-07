def pigLatin(s:str):
    string_list  = s.split(' ')
    
    for i in range(len(string_list)):
        word = string_list[i]
        word += word[0]
        semi_pig_word = word[1:]
        semi_pig_word += "ay"
        pig_word = semi_pig_word
        string_list[i] = pig_word

    pig_string = ""

    for i in string_list:
        pig_string += i
        pig_string += " "

    return pig_string
        
# ellohay otay udoswallkay

print(pigLatin("hello to kudoswall"))