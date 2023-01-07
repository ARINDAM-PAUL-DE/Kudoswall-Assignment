def alternate_case(s:str):
    alternate_string = ""
    for i in range(len(s)):
        if s[i].isupper():
            alternate_string += s[i].lower()
        else:
            alternate_string += s[i].upper()
    
    return alternate_string

print(alternate_case("altERnaTIng cAsE"))